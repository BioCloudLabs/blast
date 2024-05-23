# Define a custom exception class named Exit
class Exit(Exception):
    # Initialize the exception with a status code
    def __init__(self, status: int) -> None:
        self.status = status  # Store the status code in the instance

    # Define the string representation of the exception
    def __str__(self) -> str:
        # Dictionary mapping status codes to error messages
        MESSAGE = {
            1: 'Error in query sequence(s) or BLAST options',
            2: 'Error in BLAST database',
            3: 'Error in BLAST engine',
            4: 'Out of memory',
            5: 'Network error connecting to NCBI to fetch sequence data',
            6: 'Error creating output files'
        }
        
        # Return the error message corresponding to the status code
        return MESSAGE[self.status]
