from marshmallow import Schema
from marshmallow.fields import Raw, Str

class Files(Schema):
    query = Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)

class Form(Schema):
    db = Str(required=True)
    program = Str(required=True)