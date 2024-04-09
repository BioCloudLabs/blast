from marshmallow import Schema, post_load
from marshmallow.fields import String
from Bio import Entrez
from Bio.Entrez import efetch
from urllib.error import HTTPError
from flask_smorest import abort

class BlastSchema(Schema):
    """
    :param query:
    :param db:
    :param program:
    :param molecule:
    """
    query: String = String(required=True)
    db: String = String(required=True)
    program: String = String(required=True)
    molecule: String = String(required=True)

    @post_load
    def post_load(self, schema: dict, **kwargs: dict) -> None:
        """

        :param schema:
        :param kwargs:
        :return:
        """
        Entrez.email: str = 'info@biocloudlabs.es'

        try:
            with open(file=f"queries/{schema['query']}.fasta", mode='w+') as file:
                file.write(efetch(db=schema['molecule'], id=schema['query'], rettype='fasta').read())
        except HTTPError:
            abort(http_status_code=422)

        return schema