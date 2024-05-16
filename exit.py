class Exit(Exception):
    def __init__(self, status: int) -> None:
        self.status = status

    def __str__(self) -> str:
        MESSAGE = {
            1: 'Error in query sequence(s) or BLAST options',
            2: 'Error in BLAST database',
            3: 'Error in BLAST engine',
            4: 'Out of memory',
            5: 'Network error connecting to NCBI to fetch sequence data',
            6: 'Error creating output files'
        }
        
        return MESSAGE[self.status]