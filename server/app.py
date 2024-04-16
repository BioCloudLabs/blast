import flask
import flask_smorest
import flask_cors
import blueprint
from . import socketio

app = flask.Flask(__name__)

app.config['API_TITLE'] = 'blast/api'
app.config['API_VERSION'] = '0.0.1'
app.config['OPENAPI_VERSION'] = '3.1.0'

api = flask_smorest.Api(app)
api.register_blueprint(blueprint.blueprint)

socketio.socketio.init_app(app)

flask_cors.CORS(app, resources={r'*': {'origins': '*'}})

if __name__ == '__main__':
    app.run(debug=True)