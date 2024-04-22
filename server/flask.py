from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
from blueprint import blueprint
from .flask_socketio import flask_socketio
from typing import Dict
from requests import get

ip: str = get('https://api.ipify.org').text

API_TITLE: str = 'blast/api'
API_VERSION: str = '0.0.1'
OPENAPI_VERSION: str = '3.1.0'

RESOURCES: Dict[str, Dict[str, str]] = {
    r'*': {
        'origins': f'http://{ip}:8080'
    }
}

flask: Flask = Flask(__name__)

flask.config['API_TITLE'] = API_TITLE
flask.config['API_VERSION'] = API_VERSION
flask.config['OPENAPI_VERSION'] = OPENAPI_VERSION

flask_socketio.init_app(flask)

api: Api = Api(flask)
api.register_blueprint(blueprint)

CORS(flask, resources=RESOURCES)
