class BibliotecaServicio:
    def __init__(self):
        # Se usa un diccionario para los libros disponibles.
        # La clave es el ISBN y el valor es el objeto Libro.
        # Esto permite acceder rápido a un libro usando su ISBN.
        self._libros_disponibles = {}

        # Se usa otro diccionario para guardar los usuarios por su ID.
        # Esto ayuda a acceder rápidamnete al objeto Usuario usando el ID.
        self._usuarios = {}

        # Se usa un set para asegurar que no existan IDs repetidos.
        self._ids_registrados = set()


    def _buscar_libro_prestado(self, isbn):
        # Este método privado revisa en todos los usuarios si un libro
        # con ese ISBN está prestado.
        # Es privado porque solo se usa dentro del servicio.
        for usuario in self._usuarios.values():
            for libro in usuario.get_libros_prestados():
                if libro.get_isbn() == isbn:
                    return libro
        return None