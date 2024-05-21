from flask_smorest import Blueprint, abort
from container import Container
from schema.files import Files
from schema.form import Form
from typing import Dict
from werkzeug.datastructures import FileStorage
from exit import Exit
from flask.views import MethodView
from os.path import exists

blueprint = Blueprint('blast', __name__)

@blueprint.route('/blast')
class Blast(MethodView, Container):
    @blueprint.arguments(Files, location='files')
    @blueprint.arguments(Form, location='form')
    @blueprint.response(200)
    def post(self, files: Dict[str, FileStorage], form: Dict[str, str]) -> None:
        """
        :param files:
        :param form:
        """
        if not exists(f"results/{form['out']}"):
            try:
                self.run(files['query'].filename, form['db'], form['out'])
            except Exit as message:
                abort(400, message=message.__str__())
        else:
            abort(400, message='BLAST output name already exists')