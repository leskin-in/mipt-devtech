#!/usr/bin/env python3

import pika
import time
from pymongo import MongoClient


Q_NAME = 'mongo'


def callback(ch, method_frame, properties, body):
    cli = MongoClient('mongodb')
    db = cli.test
    coll = db[Q_NAME]
    message = str(body)
    coll.insert_one({'rcv': message})
    ch.basic_ack(delivery_tag=method_frame.delivery_tag)

def main():
    channel = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq')).channel()
    channel.queue_declare(queue=Q_NAME)
    channel.basic_consume(callback, queue=Q_NAME)
    channel.start_consuming()


if (__name__ == '__main__'):
    time.sleep(30)
    main()
