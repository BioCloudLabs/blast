from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
from blueprint import blueprint
from socket import socket

app = Flask(__name__)

app.config['API_TITLE'] = 'blast/api'
app.config['API_VERSION'] = '0.0.1'
app.config['OPENAPI_VERSION'] = '3.1.0'

websocket.init_app(app)

api = Api(app)
api.register_blueprint(blueprint)

CORS(app, resources={r'*': {'origins': '*'}})
