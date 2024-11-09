import smtplib
import os
import json
from email.message import EmailMessage

def notification(message):
    message = json.loads(message)
    mp3_fid = message['mp3_fid']
    sender_address = os.environ.get('GMAIL_ADDRESS')
    sender_password = os.environ.get('GMAIL_PASSWORD')
    reciever_address = os.environ.get('username')

    try:
        msg = EmailMessage()
        msg.set_content(f'mp3 file_id: {mp3_fid} is now ready.')
        msg['Subject'] = 'MP3 Download'
        msg['From'] = sender_address
        msg['To'] = reciever_address

        with smtplib.SMTP('smtp.gmail.com', 587) as session:
            session.starttls()
            session.login(sender_address, sender_password)
            session.send_message(msg, sender_address, reciever_address)
            session.quit()
            print('Mail Sent Successfully')

    except Exception as err:
        return err