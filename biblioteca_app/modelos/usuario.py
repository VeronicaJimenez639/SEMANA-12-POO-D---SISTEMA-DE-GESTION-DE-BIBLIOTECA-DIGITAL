class Usuario:
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre  # Nombre del usuario registrado en la biblioteca.
        self._id_usuario = id_usuario # ID único del usuario.
        self._libros_prestados = [] # Se usa lista porque los préstamos pueden cambiar: se agregan y se eliminan.

# Getters para acceder a los atributos del usuario.
    def get_nombre(self):
        return self._nombre

    def get_id_usuario(self):
        return self._id_usuario

    def get_libros_prestados(self):
        # Se devuelve una copia de la lista para proteger el encapsulamiento.
        # Así no se modifica directamente desde fuera de la clase.
        return list(self._libros_prestados)
    
# Métodos para manejar los libros prestados por el usuario.
    def prestar_libro(self, libro):
        # Agrega un libro a la lista de libros prestados del usuario.
        self._libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        # Recorre la lista para encontrar el libro por ISBN.
        # Si lo encuentra, lo elimina de la lista y lo devuelve.
        for libro in self._libros_prestados:
            if libro.get_isbn() == isbn:
                self._libros_prestados.remove(libro)
                return libro

        # Si no lo encuentra, retorna None.
        return None

    def tiene_libros_prestados(self):
        # Sirve para validar si un usuario puede ser eliminado o no.
        return len(self._libros_prestados) > 0
   
    def __str__(self):
        return f"Usuario: {self.get_nombre()} | ID: {self.get_id_usuario()}"
