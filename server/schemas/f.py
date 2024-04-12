from marshmallow import Schema, post_load, validates_schema, ValidationError
from marshmallow.fields import Raw
from werkzeug.datastructures import FileStorage
from typing import Dict, Any
from uuid import UUID, uuid4

class FSchema(Schema):
    f: Raw = Raw(metadata={'type': 'string', 'format': 'binary'})

    uuid: UUID = uuid4()

    @post_load
    def post_load(self, data: Dict[str, FileStorage], **kwargs: Dict[str, Any]) -> Dict[str, FileStorage]:
        f: FileStorage = data['f']

        if f:
            f.save(dst=f"queries/{self.uuid}.fasta")

        return data

    @validates_schema
    def validates_schema(self, data: Dict[str, FileStorage], **kwargs: Dict[str, Any]) -> None:
        f: FileStorage = data['f']

        if f:
            if not f.filename.endswith(('.fasta', '.fas', '.fa', '.fna', '.ffn', '.faa', '.mpfa', 'frn')):
                raise ValidationError(message='')

    