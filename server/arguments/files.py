import marshmallow
import marshmallow.fields
import re

class FilesSchema(marshmallow.Schema):
    query = marshmallow.fields.Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)

    @marshmallow.validates('query')
    def validates(self, query):
        """
        Validates the query file

        :param query: 
        """
        if not query.filename.endswith(('.fasta', '.fas', '.fa', '.fna', '.ffn', '.faa', '.mpfa', 'frn')):
            raise marshmallow.ValidationError('FASTA filename extension error')
        
        if not re.match(r'^>.*\s*\n[A-Za-z\n**-]+$', query.stream.read().decode()):
            raise marshmallow.ValidationError('FASTA format error')
        
        query.stream.seek(0)
    
    @marshmallow.post_load
    def post_load(self, schema, **kwargs):
        """
        Post-load method to save the query file

        :param schema: request files object 
        :return: request files object
        """
        schema['query'].save(f"queries/{schema['query'].filename}")  

        return schema

