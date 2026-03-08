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
