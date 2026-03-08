class Usuario:
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre  # Nombre del usuario registrado en la biblioteca.
        self._id_usuario = id_usuario # ID único del usuario.
        self._libros_prestados = [] # Se usa lista porque los préstamos pueden cambiar: se agregan y se eliminan.

