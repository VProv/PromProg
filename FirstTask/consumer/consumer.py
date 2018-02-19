import pika
import logging
import pymongo
from logging.handlers import WatchedFileHandler
from pymongo import MongoClient
import time
time.sleep(30)
client = MongoClient('localhost')
db = client.test_database
posts = db.posts


# Set up logging
handler = WatchedFileHandler("/code/worker.log")
log = logging.getLogger()
log.addHandler(handler)
logging.info('Consumer started')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    log.info("Message received: {}".format(body))
    with open("testfile.txt", "w") as f:
        f.write(" [x] Received %r" % body)
    post = str(body)
    posts.insert_one(post)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

log.info('Waiting for messages')
logging.info('Consuming started')

channel.start_consuming()
