import os
import pika 
import sys
from send import email

def main():
    def callback(ch, method, properties, body):
        err = email.notification(body)
        if err:
            print(f'Internal Server Error:\n{err}')
            ch.basic_nack(
                delivery_tag=method.delivery_tag
            )
        else:
            print('Notification Sent')
            ch.basic_ack(
                delivery_tag=method.delivery_tag
            )

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq-service')
    )
    channel = connection.channel()
    channel.basic_consume(
        queue=os.environ.get('MP3_QUEUE'),
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