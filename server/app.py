from quart import Quart
from flask_smorest import Api
import os
from dotenv import load_dotenv
from quart_cors import cors
from controllers.hello_world_controller import hello_world_blueprint

load_dotenv()

app = Quart(__name__)

app.config['API_TITLE'] = os.getenv('API_TITLE')
app.config['API_VERSION'] = os.getenv('API_VERSION')
app.config['OPENAPI_VERSION'] = os.getenv('OPENAPI_VERSION')

api = Api(app)
api.register_blueprint(hello_world_blueprint)

cors(app, allow_origin='*')