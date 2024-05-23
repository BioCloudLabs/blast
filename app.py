from flask import Flask  # Importing Flask to create the web application
from flask_smorest import Api  # Importing Api from flask_smorest to handle API creation
from blast import blueprint  # Importing the blueprint from a module named 'blast'
from flask_cors import CORS  # Importing CORS to handle Cross-Origin Resource Sharing
from json import load  # Importing load from json to read configuration files
from os import getcwd  # Importing getcwd from os to get the current working directory

# Create a Flask application instance
# Setting the static_folder and static_url_path to serve static files from a specific directory
app = Flask(__name__, static_folder=f'{getcwd()}/static/dist/', static_url_path='/')

# Define a route for the root URL ('/')
@app.route('/')
def view():
    # Serve the index.html file when the root URL is accessed
    return app.send_static_file('index.html')

# Enable CORS for all routes and origins
CORS(app, resources={r'*': {'origins': '*'}})

# Load configuration from a JSON file named 'config.json'
app.config.from_file('config.json', load=load)

# Create an API instance and associate it with the Flask application
api = Api(app)
# Register the blueprint with the API
api.register_blueprint(blueprint)

# Run the application on host '0.0.0.0' if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0')


