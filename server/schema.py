from marshmallow import Schema, post_load, ValidationError
from marshmallow.fields import String
from Bio import Entrez
from Bio.Entrez import efetch
from urllib.error import HTTPError

class BlastSchema(Schema):
    """
    :param query:
    :param db:
    :param program:
    """
    id: String = String(required=True)
    blastdb: String = String(required=True)
    program: String = String(required=True)
    db: String = String(required=True)

    @post_load
    def post_load(self, schema: dict, **kwargs: dict) -> None:
        """

        :param schema:
        :param kwargs:
        :return:
        """
        Entrez.email: str = 'info@biocloudlabs.es'
        
        try:
            with open(file='queries/query.fasta', mode='w+') as file:
                file.write(efetch(db=schema['db'], id=schema['id'], rettype='fasta').read())
        except HTTPError:
            raise ValidationError(message='')
        return schema