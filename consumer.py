from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "information_user",
        bootstrap_server = '127.0.0.1:9092',
        auto_offset_reset = 'earliest',
        group_id = "consumer-group-a"
    )
    print("start consume ... ")
    
    for msg in consumer :
        print("information = {}".format(json.loads(msg.value)))
