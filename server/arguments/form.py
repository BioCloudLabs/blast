import marshmallow
import marshmallow.fields
import marshmallow.validate

class FormSchema(marshmallow.Schema):
    database = marshmallow.fields.Str(
        required=True,
        error_messages={'required': 'BLAST database field is required'}
    )

    program = marshmallow.fields.Str(
        required=True,
        error_messages={'required': 'BLAST program field is required'},
        validate=marshmallow.validate.OneOf(
            ['blastp', 'blastn', 'blastx', 'tblastn'],
            error='BLAST program not found'
        )
    )



