import pika
import json
import tempfile 
import os
import moviepy.editor as editor
from bson.objectid import ObjectId

def start(message, fs_videos, fs_mp3s, channel):
    message = json.loads(message)
    out = fs_videos.get(ObjectId(message['video_fid']))

    tf = tempfile.NamedTemporaryFile()
    tf.write(out.read())
    audio = editor.VideoFileClip(tf.name).audio
    tf.close()
    audio_file_path = tempfile.gettempdir() + f'/{message["video_fid"]}.mp3'
    audio.write_audiofile(audio_file_path)
    audio.close

    f = open(audio_file_path, 'rb')
    data= f.read()
    fid = fs_mp3s.put(data)
    f.close()
    os.remove(audio_file_path)

    message['mp3_fid'] = str(fid)

    try:
        channel.basic_publish(
            exchange='',
            routing_key=os.environ.get('MP3_QUEUE'),
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
    except Exception as err:
        fs_mp3s.delete(fid)
        return None, err
    else:
        return str(fid), None