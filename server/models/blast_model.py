from marshmallow import Schema, validate, validates, ValidationError
from marshmallow.validate import OneOf, Regexp
from marshmallow.fields import Raw, String
from werkzeug.datastructures import FileStorage
from typing import Optional, List
from Bio import Entrez
from Bio.Entrez import efetch
from urllib.error import HTTPError
from re import match

class Blast:
    def __init__(self, sequence: str, database: str, algorithm: str, fasta: Optional[FileStorage], genbank: Optional[str]) -> None:
        """
        :param sequence: FASTA sequence to compare
        :param database: NCBI database to fetch
        :param algorithm: BLAST algorithm to calculate
        :param fasta: FASTA file to compare
        :param genbank: GenBank accession number to fetch and compare
        """
        self.sequence: str = sequence
        self.database: str = database
        self.algorithm: str = algorithm
        self.fasta: Optional[FileStorage] = fasta
        self.genbank: Optional[str] = genbank

class BlastModel(Schema):
    sequence: String = String(validate=Regexp(regex=r'^>?(\S+)\s*(.+)?$', error='Invalid FASTA sequence pattern'), required=True)

    fasta: Raw = Raw(metadata={'type': 'string','format': 'binary'})

    genbank: String = String(validate=Regexp(regex=r'[A-Z]{2}_?\d+(\.\d+)?', error='Invalid GenBank pattern'))

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
    ], error='NCBI database not found'), required=True)

    algorithm: String = String(validate=OneOf(choices=['blastn', 'blastp'], error='BLAST algorithm not found'), required=True)

    @staticmethod
    def save(sequence: str) -> None:
        """
        Writes FASTA sequence and saves FASTA file

        :param sequence: FASTA sequence to write
        """
        with open(file='files/sequence.fasta', mode='w') as fasta:
            fasta.write(__s=sequence)

    @validates('genbank')
    def validates_genbank(self, genbank: str) -> None:
        """
        Fetchs GenBank accession number to gets FASTA file and writes FASTA sequence

        :param genbank: GenBank accession number to fetch
        """
        if genbank:
            try:
                Entrez.email: str = 'info@biocloudlabs.es'

                BlastModel.save(sequence=efetch(db='nuccore', id=genbank, rettype='fasta').read())
            except HTTPError:
                raise ValidationError(message='GenBank not found')

    @validates('sequence')
    def validates_sequence(self, sequence: str) -> None:
        """
        Writes FASTA sequence

        :param sequence: FASTA sequence to write
        """
        BlastModel.save(sequence=sequence)

    @validates('fasta')
    def validates_fasta(self, fasta: FileStorage) -> None:
        """
        Validates FASTA file content and saves FASTA sequence

        :param fasta: FASTA file to save
        """
        if fasta:
            if not match(pattern=r'^>(\S+)\s+(.+)$', string=fasta.stream.read().decode()):
                raise ValidationError(message='Invalid FASTA sequence pattern')

            fasta.save(dst='files/sequence.fasta')



