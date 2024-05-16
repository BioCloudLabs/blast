from docker.errors import ContainerError
from docker import from_env
from exit import Exit

class Container:
    @staticmethod
    def run(query: str, db: str, out: str) -> None:
        """
        :param query:
        :param db:
        :param out:
        :param cwd:
        """
        try:
            from_env().containers.run(
                'ncbi/blast',
                f'blastn -query /blast/queries/{query} -db {db} -out /blast/results/{out} -html',
                remove=True,
                volumes=[
                    f'/home/azure/blastdb:/blast/blastdb',
                    f'/home/azure/queries:/blast/queries',
                    f'/home/azure/results:/blast/results'
                ]
            )
        except ContainerError as container:
            raise Exit(container.exit_status)
