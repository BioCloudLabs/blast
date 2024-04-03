from marshmallow import Schema, validate, validates, ValidationError
from marshmallow.validate import OneOf, Regexp
from marshmallow.fields import Raw, String
from werkzeug.datastructures import FileStorage
from typing import Optional
from Bio import Entrez
from Bio.Entrez import efetch
from urllib.error import HTTPError
from re import match
from os.path import exists


class Blast:
    def __init__(
        self: Blast,
        sequence: str,
        database: str,
        algorithm: str,
        file: Optional[FileStorage] = None,
        genbank: Optional[str] = None
    ) -> None:
        """
        :param sequence: FASTA sequence to compare
        :param database: NCBI database to search
        :param algorithm: BLAST algorithm to calculate statistical significance
        :param file: FASTA file sequence to compare
        :param genbank: GenBank FASTA sequence to compare
        """
        self.sequence: str = sequence
        self.database: str = database
        self.algorithm: str = algorithm
        self.file: FileStorage | None = file
        self.genbank: str | None = genbank


class BlastModel(Schema):
    sequence: String = String(
        validate=Regexp(
            # optional character, one or more non-whitespace characters, and optionally any character sequence
            regex=r'^>?(\S+)\s*(.+)?$',
            error=''
        ),
        required=True
    )

    file: Raw = Raw(
        metadata={
            'type': 'string',
            'format': 'binary'
        }
    )

    genbank: String = String(
        validate=Regexp(
            # two uppercase letters, optional underscore, one or more digits, optionally a decimal point and one or more digits
            regex=r'[A-Z]{2}_?\d+(\.\d+)?',
            error=''
        )
    )

    database: String = String(
        validate=OneOf(
            choices=[
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
            ],
            error=''
        ),
        required=True
    )

    algorithm: String = String(
        validate=OneOf(
            choices=[
                'blastn',
                'blastp',
                'blastx',
                'tblastn',
                'tblastx'
            ],
            error=''
        ),
        required=True
    )

    @validates('genbank')
    def validates_genbank(
        self: BlastModel,
        genbank: str
    ) -> None:
        """
        Searchs GenBank FASTA file and saves it

        :param genbank: GenBank to search
        :return: None
        """
        try:
            Entrez.email: str = 'info@biocloudlabs.es'
            with open(
                file='files/sequence.fasta',
                mode='w'
            ) as file:
                file.write(__s=efetch(
                    db='nuccore',
                    id=genbank,
                    rettype='fasta'
                ).read())
        except HTTPError:
            raise ValidationError(message='')

    @validates('sequence')
    def validates_sequence(
        self: BlastModel,
        sequence: str
    ) -> None:
        """
        :param sequence:
        :return:
        """
        with open(
            file='files/sequence.fasta',
            mode='w'
        ) as file:
            file.write(__s=sequence)


    @validates('file')
    def validates_file(
        self: BlastModel,
        file: FileStorage
    ) -> None:
        """
        :param file: FASTA file
        :return:
        """
        if not file.filename.endswith(__suffix=(
            '.fasta',
            '.fas',
            '.fa',
            '.fna',
            '.ffn',
            '.faa',
            'mpfa',
            'frn'
        )):
            raise ValidationError(message='')

        if not match(
            pattern=r'^>(\S+)\s+(.+)$',
            string=file.stream.read().decode()
        ):
            raise ValidationError(message='')

        file.save('files/sequence.fasta')



