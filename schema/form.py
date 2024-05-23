from marshmallow import Schema  # Importing Schema for defining data schemas
from marshmallow.fields import String  # Importing String for handling string data

# Define a schema for validating form data
class Form(Schema):
    # Define a required string field named 'db' for the database name
    db = String(required=True)
    # Define a required string field named 'out' for the output filename
    out = String(required=True)
