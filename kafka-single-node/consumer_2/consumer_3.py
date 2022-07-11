import json
#from turtle import left 
#import sqlite3
from kafka import KafkaConsumer, KafkaProducer
import sqlite3
from sqlite3 import Error
import pandas as pd
import numpy as np


# Messages will be serialized as JSON 
def serializer(message_json):
    return json.dumps(message_json).encode('utf-8')

def producer(message_json):
    # Kafka Producer
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=serializer
    )
    producer.send('meu-topico-enriquecido', message_json)

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'meu-topico-inicial',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    #connection sqlite
    sqliteConnection = sqlite3.connect('/home/cmour/cp-docker-images/examples/kafka-single-node/consumer_2/01_create_db.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite") 
    #select
    sqlite_select_query = """SELECT * from TB_CLIENTE"""
    cursor.execute(sqlite_select_query)
    head_rows = cursor.fetchmany(size=2)
    records = cursor.fetchall()

    #convert para dataframe
    df = pd.DataFrame(records, columns=['COD_CLIENTE','NOME','IDADE','GERENTE_CONTA','CONTA_CORRENTE','TIPO_CONTA_CORRENTE','SCORE'])

    #loop
    for message in consumer:
        menssage_consumer = json.loads(message.value)
        #convert para dataframe
        menssage_consumer_df = pd.DataFrame(menssage_consumer, index=[0])

        #merge
        menssage_final = menssage_consumer_df.merge(df, on="CONTA_CORRENTE")
         
        #condição
        if (menssage_final['GERENTE_CONTA']=='Joao Gomes').all():
            menssage_final["enriquecido"]=True
        else:
            menssage_final["enriquecido"]=False
        
        #conversão para JSON
        message_json = menssage_final.to_json(orient='index')

        producer(message_json)



        