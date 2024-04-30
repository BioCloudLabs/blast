from flask import Flask
from flask_smorest import Api
from view import blp

app = Flask(__name__)

app.config['API_TITLE'] = 'blast'
app.config['API_VERSION'] = '0.0.1'
app.config['OPENAPI_VERSION'] = '3.1.0'

api = Api(app)
api.register_blueprint(blp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')



