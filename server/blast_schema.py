from marshmallow import Schema, post_load, ValidationError
from marshmallow.validate import OneOf
from marshmallow.fields import String
from Bio import Entrez
from Bio.Entrez import efetch
from urllib.error import HTTPError

class BlastSchema(Schema):
    """
    :param query:
    :param blastdb:
    :param program:
    :param dbname:
    """
    query: String = String(required=True)
    blastdb: String = String(required=True)
    program: String = String(validate=OneOf(choices=['blastp', 'blastn']), required=True)
    dbname: String = String(validate=OneOf(choices=['protein', 'nucleotide']), required=True)

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
                file.write(efetch(db=schema['dbname'], id=schema['query'], rettype='fasta').read())
        except HTTPError:
            raise ValidationError(message='')

        return schema