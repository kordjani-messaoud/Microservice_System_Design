import os
import gridfs
import pika
import json
from flask import Flask, request
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

server = Flask(__name__)

mongo = PyMongo(
    server, 
    uri=f"mongodb://{os.environ.get('MONGODB_ADDRESS')}:27017/videos"
    )

fs = gridfs.GridFS(mongo.db)

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
    access = json.loads(access)

    if access["admin"]:
        if len(request.files) > 1 or len(request.files) < 1:
            return "exectly 1 file required", 400

        for _, f in request.files.items():
            err = util.upload(f, fs, channel, access)
            if err:
                return err
        return "Success", 200

    else:
        return "Forbiden, Unauthorized Access", 403

@server.route("/download", methods=["GET"])
def download():
    pass

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080)