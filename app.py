from flask_socketio import SocketIO
from shutil import disk_usage
from psutil import cpu_percent, virtual_memory
from threading import Timer
from flask import Flask

app = Flask(__name__)

socketio = SocketIO(cors_allowed_origins='*')

def blast():
    socketio.emit(
        'system',
        {
            'disk': {
                'total': round(disk_usage('/').total / (1024**3), 1),
                'used': round(disk_usage('/').used / (1024**3), 1),
                'free': round(disk_usage('/').free / (1024**3), 1)
            },
            'cpu': cpu_percent(),
            'memory': virtual_memory().percent
        }
    )

    Timer(5, blast).start()

@socketio.on('blast')
def on():
    blast()


        



