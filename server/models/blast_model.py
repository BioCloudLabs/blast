from marshmallow import Schema, validate, validates, ValidationError, validates_schema
from marshmallow.validate import OneOf, Regexp
from marshmallow.fields import Raw, String
from werkzeug.datastructures import FileStorage
from typing import Optional, Dict, List
from Bio import Entrez
from Bio.Entrez import efetch
from urllib.error import HTTPError
from re import match

class BlastModel(Schema):
    """
    regex validates string starting with (^>),  one or more non-whitespace characters ((\S+)), optionally  whitespace
    (\s*) and additional characters ((.+))
    """
    sequence_regex: str = r'^>?(\S+)\s*(.+)$'
    sequence_error: str = 'Invalid sequence pattern'
    sequence_required: bool = True
    # fasta sequence to compare
    sequence: String = String(validate=Regexp(regex=sequence_regex, error=sequence_error), required=sequence_required)

    fasta_metadata: Dict[str, str] = {'type': 'string', 'format': 'binary'}
    fasta_required: bool = False
    # fasta file to compare
    fasta: Raw = Raw(metadata=fasta_metadata, required=fasta_required)

    """
    regex validates string starting with two uppercase letters (^[A-Z]{2}), optional underscore (_?) and one or more 
    digits (\d+), optionally dot and one or more digits ((\.\d+)?)
    """
    genbank_regex: str = r'^[A-Z]{2}_?\d+(\.\d+)?'
    genbank_error: str = 'Invalid GenBank accession number pattern'
    genbank_required: bool = False
    # genbank accession number to fetch
    genbank: String = String(validate=Regexp(regex=genbank_regex, error=genbank_error), required=genbank_required)

    """
    nr is a non-redundant protein sequence ncbi database 
    nt is a non-redundant nucleotide sequence ncbi database
    """
    database_choices: List[str] = ['nt', 'nr']
    database_error: str = 'NCBI database not found'
    database_required: bool = True
    # ncbi database to fetch
    database: String = String(validate=OneOf(choices=database_choices, error=database_error), required=database_required)

    """
    blastp program fetch nr database using a protein query
    blastn program fetch nt database using a nucleotide query
    """
    program_choices: List[str] = ['blastn', 'blastp']
    program_error: str = 'BLAST program not found'
    program_required: bool = True
    # blast program to calculate
    program: String = String(validate=OneOf(choices=program_choices, error=program_error), required=program_required)

    @staticmethod
    def save(sequence: str) -> None:
        """
        open fasta file, writes fasta sequence and saves it
        :param sequence: FASTA sequence to save
        :return: None
        """
        file: str = 'files/sequence.fasta' # fasta sequence filepath
        mode: str = 'w'
        with open(file=file, mode=mode) as fasta:
            fasta.write(__s=sequence)

    @validates_schema
    def genbank(self, model: Dict[str, str | FileStorage]) -> None:
        """
        fetchs genbank accession number to get the fasta sequence and saves it
        :param genbank: genbank accession number to fetch
        :return: None
        """
        Entrez.email: str = 'info@biocloudlabs.es' # email required for fetching in entrez database

        # databases available according to the program
        DB: Dict[str, str] = {'blastp': 'protein', 'blastn': 'nucleotide'}
        id: str = model['genbank']
        RETTYPE: str = 'fasta' # response file type

        if id: # validates genbank accession number content
            try:
                # fetchs genbank accession number to get the fasta sequence
                sequence: str = efetch(db=DB[model['program']], id=id, rettype=RETTYPE).read()
                BlastModel.save(sequence=sequence) # saves the fasta sequence
            except HTTPError:
                message: str = 'GenBank accession number not found'
                raise ValidationError(message=message)

    @validates('sequence')
    def sequence(self, sequence: str) -> None:
        """
        saves fasta sequence
        :param sequence: fasta sequence to save
        :return: None
        """
        BlastModel.save(sequence=sequence)

    @validates('fasta')
    def fasta(self, fasta: FileStorage) -> None:
        """
        validates fasta sequence and saves it
        :param fasta: fasta file to validate fasta sequence and save
        :return: None
        """
        if fasta is not None:
            """
            regex validates string starting with (^>),  one or more non-whitespace characters ((\S+)), whitespace (\s*) 
            and additional characters ((.+))
            """
            pattern: str = r'^>(\S+)\s+(.+)$'
            string: str = fasta.stream.read().decode() # fasta sequence

            if not match(pattern=pattern, string=string): # validates fasta sequence
                message: str = 'Invalid FASTA file content pattern'
                raise ValidationError(message=message)

            dst: str = 'files/sequence.fasta' # fasta sequence filepath
            fasta.save(dst=dst) # saves the fasta sequence



