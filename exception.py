class Exception(Exception):
    def __init__(self, status: int) -> None:
        self.status = status

    def __str__(self) -> str:
        match self.status:
            case 1:
                return 'Error in query sequence(s) or BLAST options'
            case 2:
                return 'Error in BLAST database'
            case 3:
                return 'Error in BLAST engine'
            case 4:
                return 'Out of memory'
            case 5:
                return 'Network error connecting to NCBI to fetch sequence data'
            case 6:
                return 'Error creating output files'