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
def blast(files, form):
    """
    This function performs a BLAST search using the provided query file and form data.

    :param files: Uploaded files from the request
    :param form: Form data from the request
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
        flask_smorest.abort(400)
    except json.decoder.JSONDecodeError:
        flask_smorest.abort(400)


    

