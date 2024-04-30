from marshmallow import Schema, post_load
from marshmallow.fields import Raw, Str

class Files(Schema):
    query = Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)

    @post_load
    def fn(self, data, **kwargs):
        query = data.get('query')
        query.save(f"queries/{query.filename}")
        return data

class Form(Schema):
    db = Str(required=True)
    program = Str(required=True)
    out = Str(required=True)