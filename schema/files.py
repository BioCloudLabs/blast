from marshmallow import Schema, validates  # Importing Schema for defining data schemas and validates for validation methods
from marshmallow.fields import Raw  # Importing Raw for handling raw file data
from werkzeug.datastructures import FileStorage  # Importing FileStorage for handling file uploads

# Define a schema for validating files
class Files(Schema):
    # Define a field named 'query' that expects raw binary data
    query = Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)

    # Validation method for the 'query' field
    @validates('query')
    def method(self, query: FileStorage) -> None:
        # Save the uploaded file to the 'queries' directory with its original filename
        query.save(f'queries/{query.filename}')
