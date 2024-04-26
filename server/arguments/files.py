from marshmallow import Schema, post_load, validates, ValidationError
from marshmallow.fields import Raw
from re import match

class FilesSchema(Schema):
    query = Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)

    @validates('query')
    def validates(self, storage):
        """
        validates FASTA file

        :param storage: FASTA file
        """
        if not match(r'^>.*\s*\n[A-Za-z\n**-]+$', storage.stream.read().decode()):
            raise ValidationError('')
        
        storage.stream.seek(0)
    
    @post_load
    def post_load(self, object, **kwargs):
        """
        saves FASTA file

        :param object: request files object 
        :return: request files object
        """
        object['query'].save(f"queries/{object['query'].filename}")

        return object

