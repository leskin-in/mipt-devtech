#!/usr/bin/env python3

import pika


Q_NAME = 'mongo'


def main():
    bc = pika.BlockingConnection()
    # bc = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = bc.channel()
    channel.queue_declare(queue=Q_NAME)
    
    while True:
        try:
            message = input("MSG: ")
            channel.basic_publish('', Q_NAME, message)
            print("Message sent")
        except KeyboardInterrupt:
            bc.close()
			print()
            exit(0)


if (__name__ == '__main__'):
    main()
