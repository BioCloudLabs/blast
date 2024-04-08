from flask_smorest import Blueprint
from flask.views import MethodView
from typing import Dict
from blast_schema import BlastSchema
from python_on_whales import DockerClient
from os import getcwd

blast_blueprint: Blueprint = Blueprint(name='blast_blueprint', import_name=__name__)

@blast_blueprint.route(rule='/blast')
class BlastView(MethodView):
    @blast_blueprint.arguments(schema=BlastSchema)
    @blast_blueprint.response(status_code=200)
    def post(self, data: Dict[str, str]) -> Dict[str, str]:
        """

        :param data:
        :return:
        """
        docker_client: DockerClient = DockerClient().run(
            image='ncbi/blast',
            remove=True,
            volumes=[
                (f'{getcwd()}/queries', '/blast/queries'),
                (f'{getcwd()}/blastdb', '/blast/blastdb'),
                (f'{getcwd()}/results', '/blast/results')
            ]
        )

        docker_client.execute(
            command=f"update"
        )

