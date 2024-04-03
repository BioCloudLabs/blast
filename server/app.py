from quart import Quart
from flask_smorest import Api
from os import getenv
from dotenv import load_dotenv
from quart_cors import cors

load_dotenv()

app: Quart = Quart(__name__)

app.config['API_TITLE'] = getenv('API_TITLE')
app.config['API_VERSION'] = getenv('API_VERSION')
app.config['OPENAPI_VERSION'] = getenv('OPENAPI_VERSION')

api: Api = Api(app)

cors(app, allow_origin='*')