from flask_smorest import Blueprint, abort
from container import Container
from .resource.files import Files
from .resource.form import Form
from typing import Dict
from werkzeug.datastructures import FileStorage
from exception import Exception
from os import getcwd

blueprint = Blueprint('blast', __name__)

@blueprint.route('/blast')
class Controller(Container):
    @blueprint.arguments(Files, location='files')
    @blueprint.arguments(Form, location='form')
    @blueprint.response(200)
    def endpoint(self, files: Dict[str, FileStorage], form: Dict[str, str]) -> None:
        """
        :param files:
        :param form:
        """
        try:
            self.run(files['query'].filename, form['db'], form['out'], getcwd())
        except Exception as message:
            abort(400, message=message)