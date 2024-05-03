from flask import Flask
from flask_smorest import Api
from blueprint import blp
from flask_cors import CORS
from os import getcwd

app = Flask(__name__, static_folder=f'{getcwd()}/static/dist', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

CORS(app, resources={r'*': {'origins': '*'}})

app.config['API_TITLE'] = 'blast'
app.config['API_VERSION'] = '0.0.1'
app.config['OPENAPI_VERSION'] = '3.1.0'

api = Api(app)
api.register_blueprint(blp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')



