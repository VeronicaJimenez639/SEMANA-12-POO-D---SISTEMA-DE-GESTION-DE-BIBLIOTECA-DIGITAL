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
    
    def _obtener_todos_los_libros(self):
        # Reúne los libros disponibles y también los prestados.
        # Esto permite buscar en todo el catálogo, no solo en los disponibles.
        todos_los_libros = []

        # Este set evita duplicar libros al reunirlos.
        isbns_vistos = set()

        # Primero agrega los libros disponibles.
        for libro in self._libros_disponibles.values():
            todos_los_libros.append(libro)
            isbns_vistos.add(libro.get_isbn())

        # Luego agrega los libros prestados, si todavía no fueron añadidos.
        for usuario in self._usuarios.values():
            for libro in usuario.get_libros_prestados():
                if libro.get_isbn() not in isbns_vistos:
                    todos_los_libros.append(libro)
                    isbns_vistos.add(libro.get_isbn())

        return todos_los_libros
    
    def agregar_libro(self, libro):
        isbn = libro.get_isbn()

        # Se valida que el ISBN no exista ni en disponibles ni en préstamo.
        if isbn in self._libros_disponibles or self._buscar_libro_prestado(isbn):
            return "Ya existe un libro con ese ISBN."

        self._libros_disponibles[isbn] = libro
        return "Libro agregado correctamente."