import datetime
from app_config import *
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from models import *
from os import environ
from redis import Redis

ENVIRONMENT_DEV = 'dev'
ENVIRONMENT_LIVE = 'live'
ENVIRONMENT_TEST = 'test'

env = environ('ENVIRONMENT') if 'ENVIRONMENT' in environ else ENVIRONMENT_DEV


app = Flask(__name__)

if env == ENVIRONMENT_LIVE:
    app.config_class.from_object(ProductionConfig)
else:
    app.config_class.from_object(DevelopmentConfig)

mongo = PyMongo(app)
redis = Redis(app.config.get('REDIS_HOST'), app.config.get('REDIS_PORT'))



@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'POST':
        user_info = request.json

        for field in ['first_name', 'last_name', 'email', 'password']:
            if field not in request.json:
                return jsonify({'message', 'REQUIRRED FIELDS, first_name, last_name, email, password'}), 500

        new_user = User(
            first_name = user_info['first_name'],
            last_name = user_info['last_name'],
            email = user_info['email'],
            password = user_info['password'],
            created = datetime.datetime.now()
        ).save()

        return jsonify({'status': 'OK', '_id': new_user.id_field}), 201
    elif request.method == 'GET':
        users = User.objects.all()
        return jsonify({'status': 'OK', 'users': users}), 200

@app.route('/users/<user_id>', methods=['GET', 'DELETE'])
def users(user_id):
    return jsonify({'message': "TODO"})


if __name__ == '__main__':
    app.run('http://127.0.0.1', port=5001, debug=1)