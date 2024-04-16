import marshmallow
import marshmallow.fields
import re

class FilesSchema(marshmallow.Schema):
    query = marshmallow.fields.Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)

    @marshmallow.validates('query')
    def validates(self, query):
        """
        validates FASTA file

        :param query: FASTA file
        """
        if not query.filename.endswith(('.fasta', '.fas', '.fa', '.fna', '.ffn', '.faa', '.mpfa', 'frn')):
            raise marshmallow.ValidationError('FASTA filename extension not allowed')
        
        if not re.match(r'^>.*\s*\n[A-Za-z\n**-]+$', query.stream.read().decode()):
            raise marshmallow.ValidationError('Invalid FASTA file format')
        
        query.stream.seek(0)
    
    @marshmallow.post_load
    def post_load(self, schema, **kwargs):
        """
        saves FASTA file

        :param schema: request files object 
        :return: request files object
        """
        schema['query'].save(f"queries/{schema['query'].filename}")  

        return schema

