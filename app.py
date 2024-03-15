from quart import Quart
from flask_smorest import Api
import os
from dotenv import load_dotenv
from flask_cors import CORS
from database import database

load_dotenv()

app: Quart = Quart(__name__)

app.config['API_TITLE'] = os.getenv('API_TITLE')
app.config['API_VERSION'] = os.getenv('API_VERSION')
app.config['OPENAPI_VERSION'] = os.getenv('OPENAPI_VERSION')

database.init_app(app)

api: Api = Api(app)

CORS(app, resources={r'*': {'origins': '*'}})

if __name__ == '__main__':
    app.run(debug=True)

