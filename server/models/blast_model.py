from marshmallow import Schema, validate, validates, ValidationError
from marshmallow.validate import OneOf, Regexp
from marshmallow.fields import Raw, String
from werkzeug.datastructures import FileStorage
from typing import Optional
from Bio import Entrez
from Bio.Entrez import efetch
from urllib.error import HTTPError
from re import match
from dataclasses import  dataclass

@dataclass
class Blast:
    sequence: str # fasta sequence to compare
    fasta: Optional[FileStorage] # fasta file to compare
    genbank: Optional[str] # genbank accession number to fetch
    database: str # ncbi database to fetch
    algorithm: str # blast algorithm to calculate

class BlastModel(Schema):
    """
    regex validates string starting with (^>),  one or more non-whitespace characters ((\S+)), optionally  whitespace
    (\s*) and additional characters ((.+))
    """
    sequence: String = String(validate=Regexp(regex=r'^>?(\S+)\s*(.+)$', error=''), required=True)

    fasta: Raw = Raw(metadata={'type': 'string','format': 'binary'})

    """
    regex validates string starting with two uppercase letters (^[A-Z]{2}), optional underscore (_?) and one or more 
    digits (\d+), optionally dot and one or more digits ((\.\d+)?)
    """
    genbank: String = String(validate=Regexp(regex=r'^[A-Z]{2}_?\d+(\.\d+)?', error=''))

    """
    nr is a non-redundant protein sequence database 
    nt is a non-redundant nucleotide sequence database
    """
    database: String = String(validate=OneOf(choices=['nt', 'nr'], error=''), required=True)

    """
    """
    algorithm: String = String(validate=OneOf(choices=['blastn', 'blastp'], error=''), required=True)

    @staticmethod
    def __save_sequence(sequence: str) -> None:
        """
        creates fasta file, writes fasta sequence and saves it in 'files/' directory as 'sequence.fasta'
        :param sequence: FASTA sequence to save
        :return: None
        """
        with open(file='files/sequence.fasta', mode='w') as fasta:
            fasta.write(__s=sequence)

    @validates('genbank')
    def validates_genbank(self, genbank: str) -> None:
        """
        fetchs genbank accession number to get the fasta file, creates fasta file, writes fasta sequence and saves it
        in the 'files/' directory as 'sequence.fasta'
        :param genbank: genbank accession number to fetch
        :return: None
        """
        if genbank:
            try:
                Entrez.email: str = 'info@biocloudlabs.es'

                """
                
                """
                BlastModel.__save_sequence(sequence=efetch(db='nuccore', id=genbank, rettype='fasta').read())
            except HTTPError:
                raise ValidationError(message='GenBank not found')

    @validates('sequence')
    def validates_sequence(self, sequence: str) -> None:
        """
        create fasta file, writes fasta sequence and saves it in 'files/' directory as 'sequence.fasta'
        :param sequence: fasta sequence to save
        :return: None
        """
        BlastModel.__save_sequence(sequence=sequence)

    @validates('fasta')
    def validates_fasta(self, fasta: FileStorage) -> None:
        """
        validates fasta file content and saves it in the 'files/' directory as 'sequence.fasta'
        :param fasta: fasta file to validate and save
        :return: None
        """
        if fasta:
            """
            regex validates string starting with (^>),  one or more non-whitespace characters ((\S+)), whitespace (\s*) 
            and additional characters ((.+))
            """
            if not match(pattern=r'^>(\S+)\s+(.+)$', string=fasta.stream.read().decode()):
                raise ValidationError(message='')

            fasta.save(dst='files/sequence.fasta')



