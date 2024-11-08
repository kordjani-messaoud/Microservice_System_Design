import os
import gridfs
import pika
import json
from flask import Flask, request, send_file
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util
from bson.objectid import ObjectId

server = Flask(__name__)

mongo_videos = PyMongo(
    server, 
    uri=f"mongodb://{os.environ.get('MONGODB_ADDRESS')}:27017/videos"
    )

mongo_mp3s = PyMongo(
    server, 
    uri=f"mongodb://{os.environ.get('MONGODB_ADDRESS')}:27017/mp3s"
    )

fs_videos = gridfs.GridFS(mongo_videos.db)
fs_mp3s = gridfs.GridFS(mongo_mp3s.db)

connection = pika.BlockingConnection(
    pika.ConnectionParameters("rabbitmq-service")
    )

channel = connection.channel()

@server.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)
    if not err:
        return token
    else:
        return err

@server.route("/upload", methods=["POST"])
def upload():
    access, err = validate.token(request)
    if err:
        return err

    access = json.loads(access)
    if access["admin"]:

        if len(request.files) > 1 or len(request.files) < 1:
            return "exectly 1 file required", 400

        for _, f in request.files.items():
            err = util.upload(f, fs_videos, channel, access)
            if err:
                return err
        return "Success", 200

    else:
        return "Forbiden, Unauthorized Access", 403

@server.route("/download", methods=["GET"])
def download():
    access, err = validate.token(request)
    if err:
        return err

    access = json.loads(access)
    if access['admin']:
        fid = request.args.get('fid')
        if not fid:
            return 'Fid Is Required', 400

    try:
        out = fs_mp3s.get(ObjectId(fid)) 
        return send_file(out, download_name=f'{fid}.mp3')
    except Exception as err:
        return f'\nInternal Server Erro:\n {err}', 400
    

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080)