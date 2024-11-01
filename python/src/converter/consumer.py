import os
import time
import pika 
import sys
import gridfs
from pymongo import MongoClient
from convert import to_mp3

def main():
    # MongoDB DB's
    client = MongoClient('host.kubernetes.internal', 27017)
    db_videos = client.videos
    db_mp3s = client.mp3s
    # GridFS
    fs_videos = gridfs.GridFS(db_videos)
    fs_mp3s = gridfs.GridFS(db_videos)

    # Callback func, the parameters are pre-defined => can't add others 
    def callback(ch, method, properties, body):
        err = to_mp3.start(body, fs_videos, fs_mp3s, ch)
        if err:
            ch.basic_nack(
                deliver_tag=method.delivery_tag
            )
        else:
            ch.basic_ack(
                deliver_tag=method.delivery_tag
            )

    # RabbitMQ Connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq-service')
    )
    channel = connection.channel()
    channel.basic_consume(
        queue=os.environ.get('VIDEO_QUEUE'),
        on_message_callback=callback
        )

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)