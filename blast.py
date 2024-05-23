from flask_smorest import Blueprint, abort  # Importing Blueprint for creating a blueprint and abort for handling errors
from container import Container  # Importing Container class, presumably contains logic related to BLAST operations
from schema.files import Files  # Importing the Files schema for validating file input
from schema.form import Form  # Importing the Form schema for validating form data
from typing import Dict  # Importing Dict type hint for type annotations
from werkzeug.datastructures import FileStorage  # Importing FileStorage for handling file uploads
from exit import Exit  # Importing custom Exit exception class
from flask.views import MethodView  # Importing MethodView to create class-based views
from os.path import exists  # Importing exists to check if a file path exists

# Creating a Blueprint named 'blast'
blueprint = Blueprint('blast', __name__)

# Defining a class-based view for the '/blast' route
@blueprint.route('/blast')
class Blast(MethodView, Container):
    @blueprint.arguments(Files, location='files')  # Specifying that file arguments should be validated with the Files schema
    @blueprint.arguments(Form, location='form')  # Specifying that form arguments should be validated with the Form schema
    @blueprint.response(200)  # Specifying a successful response with status code 200
    def post(self, files: Dict[str, FileStorage], form: Dict[str, str]) -> None:
        """
        Handles POST requests to the /blast endpoint.
        :param files: Dictionary of uploaded files
        :param form: Dictionary of form data
        """
        # Check if the BLAST output file already exists
        if not exists(f"results/{form['out']}"):
            try:
                # If it doesn't exist, run the BLAST operation
                self.run(files['query'].filename, form['db'], form['out'])
            except Exit as message:
                # If an Exit exception occurs, abort with a 400 error and the exception message
                abort(400, message=message.__str__())
        else:
            # If the output file already exists, abort with a 400 error and a message
            abort(400, message='BLAST output name already exists')
