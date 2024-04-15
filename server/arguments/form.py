import marshmallow
import marshmallow.fields
import marshmallow.validate

class FormSchema(marshmallow.Schema):
    database = marshmallow.fields.Str(required=True)
    program = marshmallow.fields.Str(validate=marshmallow.validate.OneOf(['blastp', 'blastn', 'blastx', 'tblastn'], error=''), required=True)



