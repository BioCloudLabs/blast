from flask_smorest import Blueprint
from flask.views import MethodView
from blast_schema import BlastSchema
from json import loads
from docker import from_env
from os import getcwd

blast_blueprint: Blueprint = Blueprint(name='blast_blueprint', import_name=__name__)

@blast_blueprint.route(rule='/blast')
class BlastView(MethodView):
    @blast_blueprint.arguments(schema=BlastSchema)
    @blast_blueprint.response(status_code=200)
    def post(self, payload: dict) -> dict:
        """

        :param payload:
        :return:
        """
        return loads(from_env().containers.run(
            image='ncbi/blast',
            name='blast',
            volumes=[
                f'{getcwd()}/queries:/blast/queries',
                f'{getcwd()}/blastdb:/blast/blastdb'
            ],
            command=f"{payload['program']} -query /blast/queries/{payload['query']}.fasta -db {payload['blastdb']} -outfmt 15"
        ))

