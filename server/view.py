from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schema import BlastSchema
from json import loads
from docker import from_env
from docker.errors import ContainerError
from os import getcwd, getenv
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, BlobClient
from io import BytesIO

load_dotenv()

blast_blueprint: Blueprint = Blueprint(name='blast_blueprint', import_name=__name__)
blob_service_client = BlobServiceClient.from_connection_string(getenv('AZURE_STORAGE_CONNECTION_STRING'))

@blast_blueprint.route(rule='/blast')
class BlastView(MethodView):
    @blast_blueprint.arguments(schema=BlastSchema)
    @blast_blueprint.response(status_code=200)
    def post(self, payload: dict) -> dict:
        """

        :param payload:
        :return:
        """
        blob_client: BlobClient = blob_service_client.get_blob_client(container='blastdb', blob="pdbaa.pdb")
        stream = BytesIO()
        blob_client.download_blob().download_to_stream(stream)
        stream.seek(0)
        try:
            return loads(from_env().containers.run(
                image='ncbi/blast',
                remove=True,
                stdin=stream,
                command=f"{payload['program']} -query /blast/queries/query.fasta -db {payload['blastdb']} -outfmt 15",
            ))
        except ContainerError:
            abort(http_status_code=400)


