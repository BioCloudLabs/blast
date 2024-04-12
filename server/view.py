from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas.query import QuerySchema
from schemas.f import FSchema
from json import loads
from docker import from_env
from docker.errors import ContainerError
from os import getcwd, remove
from flask import request

blast_blueprint: Blueprint = Blueprint(name='blast_blueprint', import_name=__name__)

@blast_blueprint.route(rule='/blast')
class BlastView(MethodView):
    @blast_blueprint.arguments(schema=QuerySchema, location='form')
    @blast_blueprint.arguments(schema=FSchema, location='files')
    @blast_blueprint.response(status_code=200)
    def post(self, payload: dict) -> dict:
        """

        :param payload:
        :return:
        """
        try:
            response = loads(from_env().containers.run(
                image='ncbi/blast',
                remove=True,
                volumes=[
                    f'{getcwd()}/blastdb:/blast/blastdb',
                    f'{getcwd()}/queries:/blast/queries'
                ],
                command=f"{payload['program']} -query /blast/queries/{request.uuid}.fasta -db {payload['blastdb']} -outfmt 15",
            ))

            remove(f"queries/{request.uuid}.fasta")

            return response['BlastOutput2'][0]['report']['results']['search']['hits'] 
        except ContainerError:
            abort(http_status_code=400)






