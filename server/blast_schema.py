from marshmallow import Schema, validate, post_load
from marshmallow.validate import Regexp, OneOf
from marshmallow.fields import String
from Bio import Entrez
from Bio.Entrez import efetch
from urllib.error import HTTPError
from flask_smorest import abort
from typing import Dict, Any

class BlastSchema(Schema):
    """
    :param query:
    :param database:
    :param blast:
    :param entrez:
    """
    query: String = String(validate=Regexp(regex=r'^[A-Z]{2,3}_?\d+(\.\d+)?$'), required=True)
    database: String = String(required=True)
    blast: String = String(validate=OneOf(choices=['blastp', 'blastn', 'blastx', 'tblastn', 'tblastx']), required=True)
    entrez: String = String(validate=OneOf(choices=['protein', 'nuccore']), required=True)

    @post_load
    def post_load(self, data: Dict[str, str], **kwargs: Dict[str, Any]) -> None:
        """

        :param data:
        :param kwargs:
        :return:
        """
        Entrez.email: str = 'info@biocloudlabs.es'

        try:
            with open(file='queries/sequence.fasta', mode='w') as file:
                file.write(efetch(db=data['entrez'], id=data['query'], rettype='fasta').read())
        except HTTPError:
            abort(http_status_code=400)

        return data