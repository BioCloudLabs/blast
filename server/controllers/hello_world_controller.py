from flask_smorest import Blueprint
from quart.views import MethodView

hello_world_blueprint = Blueprint('hello_world', __name__)

@hello_world_blueprint.route('/')
class HelloWorldController(MethodView):
    hello_world_blueprint.response(200)
    async def get(self):
        return {
            'message': 'Hello, World!'
        }