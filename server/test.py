from models.blast_model import BlastModel

# Crear una instancia de BlastModel con datos de ejemplo
blast_data = {
    'sequence': 'ATCGATCGATCG',
    'database': 'nt',
    'program': 'blastn',
}

blast_model = BlastModel()


result = blast_model.load(blast_data)
print("Datos válidos:", result)
