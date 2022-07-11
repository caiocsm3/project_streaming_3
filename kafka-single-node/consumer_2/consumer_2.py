import json 
from kafka import KafkaConsumer

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'meu-topico-enriquecido',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    for message_json in consumer:
        print(json.loads(message_json.value))