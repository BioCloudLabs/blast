from marshmallow import Schema, post_load, validates, ValidationError
from marshmallow.fields import Raw
from re import match
from typing import Dict, Any
from werkzeug.datastructures import FileStorage

METADATA: Dict[str, str] = {
    'type': 'string',
    'format': 'binary'
}

PATTERN: str = r'^>.*\s*\n[A-Za-z\n**-]+$'

class FilesSchema(Schema):
    query: Raw = Raw(metadata=METADATA, required=True)

    @validates('query')
    def validates(self, storage: FileStorage):
        """
        validates FASTA file

        :param storage: FASTA file
        """
        string: str = storage.stream.read().decode()

        if not match(PATTERN, string):
            raise ValidationError('')
        
        storage.stream.seek(0)
    
    @post_load
    def post_load(self, object: Dict[str, FileStorage], **kwargs: Dict[str, Any]):
        """
        saves FASTA file

        :param object: request files object 
        :return: request files object
        """
        storage: FileStorage = object['query']

        dst: str = f'queries/{storage.filename}'

        storage.save(dst)  

        return object

