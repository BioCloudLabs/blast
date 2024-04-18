from flask_socketio import SocketIO
from shutil import disk_usage
from psutil import cpu_percent, virtual_memory
from typing import Dict

socket: SocketIO = SocketIO(cors_allowed_origins='*')

@socket.on('azure')
def handle_azure() -> Dict[str, float | Dict[str, float]]:
    total, used, free: float = round(disk_usage('/') / (1024**3), 1)

    cpu: float = cpu_percent()

    memory: float = virtual_memory().percent

    event: str = ''

    args: Dict[str, float | Dict[str, float]] = {
        'disk': {
            'total': total,
            'used': used,
            'free': free
        },
        'cpu': cpu,
        'memory': memory
    }
   
    
