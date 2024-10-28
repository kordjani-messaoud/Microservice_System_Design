import jwt
import datetime
import os
from flask import Flask, request
from flask_mysqldb import MySQL


def create_JWT(username, secret, authz):
    return jwt.encode(
        {
            'username': username,
            'exp': datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'admin': authz,
        },
        secret,
        algorithm='HS256'
    )


server = Flask(__name__)
mysql = MySQL(server)

server.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
server.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
server.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
server.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
server.config['MYSQL_PORT'] = os.environ.get('MYSQL_PORT')


@server.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth:
        return 'Unauthorized, Missing Credentials', 401

    cur = mysql.connection.cursor()
    res = cur.execute(
        f'SELECT name, email, password FROM user WHERE email {auth.username}'
    )

    if len(res) > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[0]
        if auth.username != email or auth.password != password:
            return 'Unauthorized, Invalid Credentials', 401
        else:
            return create_JWT(auth.username, os.environ.get('JWT_SECRET'), True)
    else:
        return 'Invalide credentials', 401


@server.route('/validate', methods=['POST'])
def validate():
    encoded_jwt = request.headers('Authorization')
    if not encoded_jwt:
        return 'Unauthorized, Missing Credentials', 401
    encoded_jwt = encoded_jwt.split(' ')[1]

    try:
        decoded_token = encoded_jwt.decode(encoded_jwt, os.environ.get('JWT_SECRET'),
                                           algorithms=['HS256']
                                           )
    except:
        return 'Forbidden', 403
    return decoded_token, 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000)
