from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
from blueprint import blueprint
from requests import get
from flask_socketio import SocketIO
from shutil import disk_usage
from psutil import cpu_percent, virtual_memory

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': f"http://{get('https://api.ipify.org').text}:8080"}})

app.config['API_TITLE'] = 'blast/api'
app.config['API_VERSION'] = '0.0.1'
app.config['OPENAPI_VERSION'] = '3.1.0'

api = Api(app)
api.register_blueprint(blueprint)

socketio = SocketIO(app, cors_allowed_origins='*') 

@socketio.on('azure')
def handler():
    total, used, free = round(disk_usage('/') / (1024**3), 1)

    socketio.emit(
        'disk': {
            'total': total,
            'used': used,
            'free': free
        },
        'cpu': cpu_percent(),
        'memory': virtual_memory().percent
    )

