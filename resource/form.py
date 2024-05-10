from marshmallow import Schema
from marshmallow.fields import String

class Form(Schema):
    db = String(required=True)
    out = String(required=True)