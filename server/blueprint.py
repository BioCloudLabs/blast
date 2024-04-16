import docker.errors
import flask_smorest
import json
import docker
import arguments.files
import arguments.form
import os

blueprint = flask_smorest.Blueprint('blast', __name__)

@blueprint.route('/blast', methods=['POST'])
@blueprint.arguments(arguments.files.FilesSchema, location='files')
@blueprint.arguments(arguments.form.FormSchema, location='form')
@blueprint.response(200)
def post(files, form):
    """
    runs 'ncbi/blast' docker image for local alignments

    :param files: request files object
    :param form: request form object
    :return: local aligmment object
    """
    try:
        return json.loads(
            docker.from_env().containers.run(
                'ncbi/blast',
                command=f"{form['program']} -query /blast/queries/{files['query'].filename} -db {form['database']} -outfmt 15",
                remove=True,
                volumes=[
                    f'{os.getcwd()}/blastdb:/blast/blastdb',
                    f'{os.getcwd()}/queries:/blast/queries'
                ]
            )
        )
    except docker.errors.ContainerError:
        flask_smorest.abort(400, message='')


    

