import json
#from turtle import left 
#import sqlite3
from kafka import KafkaConsumer, KafkaProducer
import sqlite3
from sqlite3 import Error
import pandas as pd
import numpy as np


# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

def producer(message):
    # Kafka Producer
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=serializer
    )
    producer.send('meu-topico-enriquecido', message)

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'meu-topico-inicial',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    #connection sqlite + select
    sqliteConnection = sqlite3.connect('/home/cmour/cp-docker-images/examples/kafka-single-node/consumer_2/01_create_db.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite") 

    sqlite_select_query = """SELECT * from TB_CLIENTE"""
    cursor.execute(sqlite_select_query)
    head_rows = cursor.fetchmany(size=2)
    records = cursor.fetchall()

    #df_series = pd.Series(records.randint(0,100,size=(10)), 
    #                    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    #print (df_series.to_frame(name='A'))


    #for row in head_rows:
        #row1 = row.to_frame()
    df = pd.DataFrame(records, columns=['COD_CLIENTE','NOME','IDADE','GERENTE_CONTA','tipo_operacao','TIPO_CONTA_CORRENTE','SCORE'])
    #print(df) 

    #loop
    for message in consumer:
        menssage_consumer = json.loads(message.value)
        #convert dataframe
        menssage_consumer_df = pd.DataFrame(menssage_consumer, index=[0])
        #print(menssage_consumer_df)
        #print(menssage_consumer_df.columns.tolist())
        print(menssage_consumer_df['tipo_operacao'])
        #join
        #menssage_final =pd.merge(menssage_consumer_df, df, how="inner", on=["tipo_operacao","CONTA_CORRENTE"])
        menssage_final = menssage_consumer_df.merge(df, on="tipo_operacao")

        #menssage_final = pd.merge(menssage_consumer_df, df, on=["conta","CONTA_CORRENTE"],how="inner")
        #
        
        #print(menssage_consumer_df)
        if menssage_consumer["tipo_operacao"] == "Saque":
            menssage_consumer["enriquecido"]=True
        else:
            menssage_consumer["enriquecido"]=False
        producer(menssage_consumer)

        