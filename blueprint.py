from docker.errors import ContainerError
from docker import from_env
from flask_smorest import Blueprint, abort
from arguments import Files, Form
from flask import send_file
from os import getcwd
from tempfile import NamedTemporaryFile
from os.path import basename, dirname
from io import BytesIO

blueprint = Blueprint('blast', __name__)

@blueprint.route('/blast', methods=['POST'])
@blueprint.arguments(Files, location='files')
@blueprint.arguments(Form, location='form')
@blueprint.response(200)
def view(files, form):
    """
    runs ncbi/blast docker image
    :param files: request files object 
    :param form: request form object
    """
    with NamedTemporaryFile(suffix='.fasta') as temporary_file:
        temporary_file.write(files.get('query').stream.read())
        temporary_file.seek(0)

        try:
            container = from_env().containers.run(
                'ncbi/blast',
                f"{form.get('program')} -query /blast/queries/{basename(temporary_file.name)} -db {form.get('db')}",
                remove=True,
                volumes=[
                    f'{getcwd()}/blastdb:/blast/blastdb',
                    f'{dirname(temporary_file.name)}:/blast/queries'
                ]
            )
            
            return send_file(BytesIO(container), mimetype='application/octet-stream')
        except ContainerError as error:
            abort(400, message=error.exit_status)
    
