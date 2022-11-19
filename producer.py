from kafka import KafkaProducer
import json
from data import get_information_user


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

'''
def get_partition(key,value,available):
    return 0
'''
producer = KafkaProducer(bootstrap_servers = ['127.0.0.1:9092'],
                         value_serializer = json_serializer
                         #partitioner = get_partition
                        )

if __name__ == '__main__':
    while 1==1:
        information_user = get_information_user()
        print (information_user)
        producer.send("information_user",information_user)
        