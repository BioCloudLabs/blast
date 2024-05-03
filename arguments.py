from marshmallow import Schema
from marshmallow.fields import Raw, Str, Int
from marshmallow.validate import OneOf, Range

class Files(Schema):
    query = Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)

class Form(Schema):
    db = Str(required=True, validate=OneOf(['env_nt', 'env_nr']))
    program = Str(required=True, validate=OneOf(['blastp', 'blastn', 'tblastn', 'blastx']))
    outfmt = Int(required=True, validate=Range(1, 18))