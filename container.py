from docker.errors import ContainerError  # Importing ContainerError to handle exceptions from Docker container runs
from docker import from_env  # Importing from_env to interact with Docker environment
from exit import Exit  # Importing custom Exit exception class

# Define a Container class to manage Docker container operations
class Container:
    @staticmethod
    def run(query: str, db: str, out: str) -> None:
        """
        Run a Docker container with the BLAST command.
        
        :param query: Name of the query file
        :param db: Name of the database to use for BLAST
        :param out: Output file name
        """
        try:
            # Run the Docker container with specified parameters
            from_env().containers.run(
                'ncbi/blast',  # Docker image to use
                f'blastn -query /blast/queries/{query} -db {db} -out /blast/results/{out} -html',  # Command to run inside the container
                remove=True,  # Automatically remove the container when it exits
                volumes=[
                    f'/home/azure/blastdb:/blast/blastdb',  # Mount host directory to container directory for BLAST database
                    f'/home/azure/queries:/blast/queries',  # Mount host directory to container directory for query files
                    f'/home/azure/results:/blast/results'  # Mount host directory to container directory for result files
                ]
            )
        except ContainerError as container:
            # If a ContainerError occurs, raise an Exit exception with the container's exit status
            raise Exit(container.exit_status)
