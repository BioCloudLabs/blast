from quart import Quart
from flask_smorest import Api
import os
from dotenv import load_dotenv
from quart_cors import cors

load_dotenv()

app: Quart = Quart(__name__)

app = cors(app, allow_origin='*')

app.config['API_TITLE'] = os.getenv('API_TITLE')
app.config['API_VERSION'] = os.getenv('API_VERSION')
app.config['OPENAPI_VERSION'] = os.getenv('OPENAPI_VERSION')

api: Api = Api(app)

if __name__ == '__main__':
    app.run(debug=True)

