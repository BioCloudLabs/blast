from quart import Quart
from flask_smorest import Api
from os import getenv
from dotenv import load_dotenv
from quart_cors import cors
from controllers.hello_world_controller import hello_world_blueprint

load_dotenv()

app = Quart(__name__)

app.config['API_TITLE'] = getenv('API_TITLE')
app.config['API_VERSION'] = getenv('API_VERSION')
app.config['OPENAPI_VERSION'] = getenv('OPENAPI_VERSION')

api = Api(app)
api.register_blueprint(hello_world_blueprint)

cors(app, allow_origin='*')