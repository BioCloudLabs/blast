from flask_socketio import SocketIO
from shutil import disk_usage
from psutil import cpu_percent, virtual_memory
from typing import Dict

EVENT: str = 'virtual_machine'

flask_socketio: SocketIO = SocketIO(cors_allowed_origins='*')

@flask_socketio.on('azure')
def handler() -> None:
    total, used, free: float = round(disk_usage('/') / (1024**3), 1)

    cpu: float = cpu_percent()

    memory: float = virtual_memory().percent

    args: Dict[str, float | Dict[str, float]] = {
        'disk': {
            'total': total,
            'used': used,
            'free': free
        },
        'cpu': cpu,
        'memory': memory
    }

    flask_socketio.emit(EVENT, args)
   
    
