from marshmallow import Schema, validates
from marshmallow.fields import Raw
from werkzeug.datastructures import FileStorage

class Files(Schema):
    query = Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)

    @validates('query')
    def method(self, query: FileStorage) -> None:
        query.save(f'queries/{query.filename}')