from docker.errors import ContainerError
from docker import from_env
from exit import Exit

class Container:
    @staticmethod
    def run(query: str, db: str, out: str, cwd: str) -> None:
        """
        :param query:
        :param db:
        :param out:
        :param cwd:
        """
        try:
            from_env().containers.run(
                'ncbi/blast',
                f'blastp -query /blast/queries/{query} -db {db} -out /blast/results/{out} -html',
                remove=True,
                volumes=[
                    f'{cwd}/blastdb:/blast/blastdb',
                    f'{cwd}/queries:/blast/queries',
                    f'{cwd}/results:/blast/results'
                ]
            )
        except ContainerError as container:
            raise Exit(container.exit_status)
