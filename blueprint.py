from docker.errors import ContainerError
from docker import from_env
from flask_smorest import Blueprint, abort
from arguments import Files, Form
from flask import send_file
from os import getcwd
from tempfile import NamedTemporaryFile
from os.path import basename, dirname
from io import BytesIO

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
    query = files.get('query')
    program = form.get('program')
    db = form.get('db')
    outfmt = form.get('outfmt')

    with NamedTemporaryFile(suffix='.fasta') as fp:
        name = fp.name

        fp.write(query.stream.read())
        fp.seek(0)

        try:
            out = from_env().containers.run(
                'ncbi/blast',
                f"{program} -query /blast/queries/{basename(name)} -db {db} -outfmt {outfmt}",
                remove=True,
                volumes=[
                    f'{getcwd()}/blastdb:/blast/blastdb',
                    f'{dirname(name)}:/blast/queries'
                ]
            )

            return send_file(BytesIO(out), mimetype='application/octet-stream')
        except ContainerError:
            abort(400)
    
