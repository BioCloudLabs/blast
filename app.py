from flask import Flask
from flask_smorest import Api
from blast import blueprint
from flask_cors import CORS
from json import load
from os import getcwd

app = Flask(__name__, static_folder=f'{getcwd()}/static/dist/', static_url_path='/')

@app.route('/')
def view():
    return app.send_static_file('index.html')

CORS(app, resources={r'*': {'origins': '*'}})

app.config.from_file('config.json', load=load)

api = Api(app)
api.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0')




