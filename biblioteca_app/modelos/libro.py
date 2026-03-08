class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Se usa una tupla para guardar título y autor juntos para que estos datos sean inmutables.
        # Por eso se almacenan como una tupla y no como lista.
        self._titulo_autor = (titulo, autor)  
        self._categoria = categoria       # La categoría se guarda como texto normal porque solo representa una característica del libro.
        self._isbn = isbn                 # El ISBN identifica de forma única a cada libro.

        