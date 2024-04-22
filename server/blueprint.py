from docker.errors import ContainerError
from flask_smorest import Blueprint, abort
from json import loads
from docker import from_env
from arguments.files import FilesSchema
from arguments.form import FormSchema
from os import getcwd
from typing import List, Dict, Any
from werkzeug.datastructures import FileStorage

VOLUMES: List[str] = [
    f'{getcwd()}/blastdb:/blast/blastdb',
    f'{getcwd()}/queries:/blast/queries'
]

blueprint: Blueprint = Blueprint('blast', __name__)

@blueprint.route('/blast', methods=['POST'])
@blueprint.arguments(FilesSchema, location='files')
@blueprint.arguments(FormSchema, location='form')
@blueprint.response(200)
def post(files: Dict[str, FileStorage], form: Dict[str, str]) -> Dict[str, Any]:
    """
    runs 'ncbi/blast' docker image for local alignments

    :param files: request files object
    :param form: request form object
    :return: local aligmment object
    """
    query: FileStorage = files['query']

    database: str = form['database']

    program: str = form['program']

    command: str = f"{program} -query /blast/queries/{query.filename} -db {database} -outfmt 15"

    try:
        response: Dict[str, Any] = loads(from_env().containers.run('ncbi/blast', command, remove=True, volumes=VOLUMES))
    except ContainerError:
        abort(400)

    return response


    

