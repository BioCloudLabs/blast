import marshmallow
import marshmallow.fields
import re
import os

class FilesSchema(marshmallow.Schema):
    query = marshmallow.fields.Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)

    @marshmallow.validates('query')
    def validates(self, query):
        """
        Validates the query file

        :param query: The query file
        """
        if not query.filename.endswith(('.fasta', '.fas', '.fa', '.fna', '.ffn', '.faa', '.mpfa', 'frn')):
            raise marshmallow.ValidationError('s')
        
        if not re.match(r'^>.*\s*\n[A-Za-z\n**-]+$', query.stream.read().decode()):
            raise marshmallow.ValidationError('d')
        
        query.stream.seek(0)

        if os.path.exists(f'queries/{query.filename}'):
            raise marshmallow.ValidationError('')
        
    @marshmallow.post_load
    def post_load(self, schema, **kwargs):
        """
        Post-load method to save the query file

        :param schema: The schema object
        :return: The schema object
        """
        schema['query'].save(f"queries/{schema['query'].filename}")  

        return schema



