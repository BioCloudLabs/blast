from flask import Flask
from flask_smorest import Api
from os import getenv
from dotenv import load_dotenv
from flask_cors import CORS
from controllers.blast_controller import blast_blueprint

load_dotenv()

app: Flask = Flask(__name__)

app.config['API_TITLE'] = getenv(key='API_TITLE')
app.config['API_VERSION'] = getenv(key='API_VERSION')
app.config['OPENAPI_VERSION'] = getenv(key='OPENAPI_VERSION')
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api: Api = Api(app=app)
api.register_blueprint(blp=blast_blueprint)

CORS(app=app, resources={r'*': {'origins': '*'}})


if __name__ == '__main__':
    app.run(debug=True)