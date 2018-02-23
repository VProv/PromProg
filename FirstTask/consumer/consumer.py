import pika
import logging
import pymongo
from logging.handlers import WatchedFileHandler
from pymongo import MongoClient
import time

time.sleep(30)

MDB = 'MDB'
client = MongoClient(host='mongo')
client.drop_database('MDB')
db = client[MDB]
db.drop_collection('messages')
print("CONSUMER START")
# Set up logging
handler = WatchedFileHandler("/apl/worker.log")
log = logging.getLogger()
log.addHandler(handler)
logging.info('Consumer started')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    log.info("Message received: {}".format(body))
    db.messages.save({str(body): str(body)})
    print("message")


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

log.info('Waiting for messages')
logging.info('Consuming started')

channel.start_consuming()
