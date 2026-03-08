class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Se usa una tupla para guardar título y autor juntos para que estos datos sean inmutables.
        # Por eso se almacenan como una tupla y no como lista.
        self._titulo_autor = (titulo, autor)  
        self._categoria = categoria       # La categoría se guarda como texto normal porque solo representa una característica del libro.
        self._isbn = isbn                 # El ISBN identifica de forma única a cada libro.

#Getters para acceder a los atributos del libro. 
# No se definen setters porque no se espera que estos atributos cambien una vez creado el libro.

    def get_titulo(self):
        # Devuelve la primera posición de la tupla: el título.
        return self._titulo_autor[0]

    def get_autor(self):
        # Devuelve la segunda posición de la tupla: el autor.
        return self._titulo_autor[1]

    def get_categoria(self):
        return self._categoria

    def get_isbn(self):
        return self._isbn     