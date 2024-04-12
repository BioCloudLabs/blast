from marshmallow import Schema, post_load, ValidationError, validates_schema
from marshmallow.fields import String, Raw
from Bio import Entrez
from Bio.Entrez import efetch
from urllib.error import HTTPError
from uuid import uuid4
from uuid import UUID
from flask import request
from typing import Dict, Any

class QuerySchema(Schema):
    """
    :param id:
    :param f:
    :param s:
    :param blastdb:
    :param program:
    """
    id: String = String(required=False)
    s: String = String(required=False)
    blastdb: String = String(required=True)
    program: String = String(required=True)

    uuid: UUID = uuid4()

    @staticmethod
    def w(s: str, uuid: UUID) -> None:
        with open(file=f"queries/{uuid}.fasta", mode='w') as f:
            f.write(s)

    @post_load
    def post_load(self, data: Dict[str, str], **kwargs: Dict[str, Any]) -> Dict[str, str]:
        Entrez.email: str = 'info@biocloudlabs.es'
        
        request.uuid: UUID = self.uuid

        id: str = data['id']

        if id:
            try:
                db: Dict[str, str] = {
                    'blastp': 'nucleotide',
                    'blastn': 'protein',
                    'blastx': 'nucleotide',
                    'tblastn': 'protein'
                }

                QuerySchema.w(s=efetch(db=db[data['program']], id=id, rettype='fasta').read(), uuid=self.uuid)
            except HTTPError:
                raise ValidationError(message='')

        QuerySchema.w(s=data['s'], uuid=self.uuid)

        return data

    @validates_schema
    def validates_schema(self, data: Dict[str, str], **kwargs: Dict[str, Any]) -> None:
        pass
