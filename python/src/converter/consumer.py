import os
import pika 
import sys
import gridfs
from pymongo import MongoClient
from convert import to_mp3

def main():
    try:
        client = MongoClient(f"{os.environ.get('MONGODB_ADDRESS')}", 27017)
    except Exception as err:
        return f'\nError at Connecting to MongoDB:\t{err}\n'

    db_videos = client.videos
    db_mp3s = client.mp3s
    fs_videos = gridfs.GridFS(db_videos)
    fs_mp3s = gridfs.GridFS(db_mp3s)

    def callback(ch, method, properties, body):
        mp3_fid, err = to_mp3.start(body, fs_videos, fs_mp3s, ch)
        if err:
            ch.basic_nack(
                delivery_tag=method.delivery_tag
            )
            print(f'\nInternal error: {err}')
        else:
            ch.basic_ack(
                delivery_tag=method.delivery_tag
            )
            print(f'\nMP3 Audio File id: {mp3_fid}')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq-service')
    )
    channel = connection.channel()
    channel.basic_consume(
        queue=os.environ.get('VIDEO_QUEUE'),
        on_message_callback=callback
        )

    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)