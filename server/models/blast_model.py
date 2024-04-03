from marshmallow import Schema, validate, validates, ValidationError
from marshmallow.validate import OneOf, Regexp
from marshmallow.fields import Raw, String
from werkzeug.datastructures import FileStorage
from typing import Any, TextIO, Optional
from Bio import Entrez
from Bio.Entrez import efetch
from urllib.error import HTTPError
from re import match


class Blast:
    def __init__(self, fasta: str, database: str, algorithm: str, file: Optional[FileStorage] = None, genbank: Optional[str] = None) -> None:
        """

        :param fasta:
        :param database:
        :param algorithm:
        :param file:
        :param genbank:
        """
        self.fasta = fasta
        self.file = file
        self.genbank = genbank
        self.database = database
        self.algorithm = algorithm


class BlastModel(Schema):
    fasta: String = String(validate=Regexp(regex=r'', error=''), required=True)

    file: Raw = Raw(metadata={'type': 'string', 'format': 'binary'})

    genbank: String = String(validate=Regexp(regex=r'[A-Z]{2}_?\d+(\.\d+)?', error=''))

    database: String = String(validate=OneOf(choices=[
        'nr',
        'nt',
        'refseq_select_rna',
        'refseq_select_prot'
        'refseq_rna',
        'env_nr',
        'tsa_nt',
        'patnt',
        'pdbnt',
        'refseq_protein',
        'landmark',
        'swissprot',
        'pataa',
        'pdbaa',
        'env_nr',
        'tsa_nr',
        'Betacoronavirus'
    ], error=''), required=True)

    algorithm: String = String(validate=OneOf(choices=[
        'blastn',
        'blastp',
        'blastx',
        'tblastn',
        'tblastx'
    ], error=''), required=True)

    @validates('genbank')
    def validates_genbank(self: BlastModel, genbank: str) -> None:
        """

        :param genbank:
        :return:
        """
        try:
            Entrez.email: str = 'info@biocloudlabs.es'
            fasta: TextIO = efetch(db='nuccore', id=genbank, rettype='fasta')
            with open(file=f'files/{genbank}.fasta', mode='w') as file:
                file.write(__s=fasta.read())
        except HTTPError:
            raise ValidationError(message='')

    @validates('fasta')
    def validates_fasta(self: BlastModel, fasta: str) -> None:
        """

        :param fasta:
        :return:
        """
        with open(file=f"files/{match(pattern=r'[A-Z]{2}_?\d+(\.\d+)?', string=fasta).group()}.fasta") as file:
            file.write(__s=fasta)
