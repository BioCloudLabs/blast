from docker.errors import ContainerError
from docker import from_env
from flask_smorest import Blueprint, abort
from schema import Files, Form
from flask import send_file
from os import getcwd

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
    query = files.get('query').filename
    program = form.get('program')
    db = form.get('db')
    out = form.get('out')

    try:
        from_env().containers.run(
            'ncbi/blast',
            f"{program} -query /blast/queries/{query} -db {db} -out /blast/results/{out}",
            remove=True,
            volumes=[
                f'{getcwd()}/blastdb:/blast/blastdb',
                f'{getcwd()}/queries:/blast/queries',
                f'{getcwd()}/results:/blast/results'
            ]
        )
        # https://www.ncbi.nlm.nih.gov/books/NBK279684/
        return send_file(f'results/{out}', as_attachment=True)   
    except ContainerError as e:
        abort(400, message=e.exit_status)
    
