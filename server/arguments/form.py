from marshmallow import Schema
from marshmallow.fields import Str

class FormSchema(Schema):
    database = Str(required=True)
    program = Str(required=True)



