from docker.errors import ContainerError
from flask_smorest import Blueprint, abort
from json import loads
from docker import from_env
from arguments.files import FilesSchema
from arguments.form import FormSchema
from os import getcwd

blueprint: Blueprint = Blueprint('blast', __name__)

@blueprint.route('/blast', methods=['POST'])
@blueprint.arguments(FilesSchema, location='files')
@blueprint.arguments(FormSchema, location='form')
def post(files, form):
    """
    runs 'ncbi/blast' docker image for local alignments

    :param files: request files object
    :param form: request form object
    :return: local aligmment object
    """
    try:
        return loads(
            from_env().containers.run(
                'ncbi/blast',
                command=f"{form['program']} -query /blast/queries/{files['query'].filename} -db {form['database']} -outfmt 15",
                remove=True,
                volumes=[
                    f'{getcwd()}/blastdb:/blast/blastdb',
                    f'{getcwd()}/queries:/blast/queries'
                ]
            )
        ), 200
    except ContainerError:
        abort(400)


    

