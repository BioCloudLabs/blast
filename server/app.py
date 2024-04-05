from quart import Quart
from flask_smorest import Api
from os import getenv
from dotenv import load_dotenv
from quart_cors import cors

load_dotenv()

app: Quart = Quart(import_name=__name__)

app.config['API_TITLE'] = getenv(key='API_TITLE')
app.config['API_VERSION'] = getenv(key='API_VERSION')
app.config['OPENAPI_VERSION'] = getenv(key='OPENAPI_VERSION')

api: Api = Api(app=app)

cors(app_or_blueprint=app, allow_origin='*')

if __name__ == '__main__':
    app.run(debug=True)