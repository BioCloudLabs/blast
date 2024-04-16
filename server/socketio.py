import flask_socketio
import shutil
import psutil

socketio = flask_socketio.SocketIO()

@socketio.on('system')
def on():
    total, used, free = shutil.disk_usage('/')

    socketio.emit(
        '',
        {
            'disk': {
                'total': total,
                'used': used,
                'free': free
            },
            'cpu': psutil.cpu_percent(),
            'memory': psutil.virtual_memory().percent
        }
    )