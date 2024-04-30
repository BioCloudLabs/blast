from docker.errors import ContainerError
from docker import from_env
from flask_smorest import Blueprint, abort
from os import getcwd
from schema import Files, Form
from flask import Response
from tempfile import TemporaryFile

blp = Blueprint('blast', __name__)

@blp.route('/blast', methods=['POST'])
@blp.arguments(Files, location='files')
@blp.arguments(Form, location='form')
@blp.response(200)
def view(files, form):
    """
    runs ncbi/blast docker image
    :param files: request files object 
    :param form: request form object
    """
    try:
        with TemporaryFile() as fp:
            fp.write(files.get('query').stream.read())
            from_env().containers.run(
                'ncbi/blast',
                f"{form.get('program')} -query /blast/queries/{files.get('query').filename} -db {form.get('db')} -out /blast/results/{form.get('out')}.out",
                remove=True,
                volumes=[
                    f'{getcwd()}/blastdb:/blast/blastdb',
                    f'{fp.name}:/blast/queries',
                    f'{getcwd()}/results:/blast/results'
                ]
            )
    except ContainerError:
        abort(400)
    
