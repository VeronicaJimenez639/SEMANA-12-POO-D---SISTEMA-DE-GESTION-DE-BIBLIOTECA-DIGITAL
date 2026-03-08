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
    
    def eliminar_libro(self, isbn):
        # Solo se puede eliminar si está disponible.
        if isbn in self._libros_disponibles:
            del self._libros_disponibles[isbn]
            return "Libro eliminado correctamente."

        # Si está prestado, no debe eliminarse.
        if self._buscar_libro_prestado(isbn):
            return "No se puede eliminar el libro porque está prestado."

        return "Libro no encontrado."
    
    def registrar_usuario(self, usuario):
        id_usuario = usuario.get_id_usuario()

        # El set se usa para comprobar que el ID no se repita.
        if id_usuario in self._ids_registrados:
            return "El ID de usuario ya existe."

        self._usuarios[id_usuario] = usuario
        self._ids_registrados.add(id_usuario)
        return "Usuario registrado correctamente."
    
    def eliminar_usuario(self, id_usuario):
        if id_usuario not in self._usuarios:
            return "Usuario no encontrado."

        usuario = self._usuarios[id_usuario]

        # No se debe eliminar un usuario que todavía tiene libros prestados.
        if usuario.tiene_libros_prestados():
            return "No se puede eliminar el usuario porque tiene libros prestados."

        del self._usuarios[id_usuario]
        self._ids_registrados.remove(id_usuario)
        return "Usuario eliminado correctamente."
    
    def prestar_libro(self, isbn, id_usuario):
        # Primero se valida que el usuario exista.
        if id_usuario not in self._usuarios:
            return "Usuario no encontrado."

        # Luego se valida que el libro esté disponible.
        if isbn not in self._libros_disponibles:
            return "Libro no disponible."

        libro = self._libros_disponibles[isbn]
        usuario = self._usuarios[id_usuario]

        # El libro se agrega a la lista del usuario.
        usuario.prestar_libro(libro)

        # Luego se elimina de los disponibles porque ya fue prestado.
        del self._libros_disponibles[isbn]

        return "Préstamo realizado correctamente."
    
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self._usuarios:
            return "Usuario no encontrado."

        usuario = self._usuarios[id_usuario]
        libro = usuario.devolver_libro(isbn)

        # Si el libro no está en la lista del usuario, no se puede devolver.
        if libro is None:
            return "Ese usuario no tiene prestado ese libro."

        # Si sí lo tenía, vuelve al diccionario de disponibles.
        self._libros_disponibles[isbn] = libro
        return "Devolución realizada correctamente."
    
    def buscar_libros_por_titulo(self, titulo):
        resultados = []

        # Se busca en todo el catálogo reunido.
        for libro in self._obtener_todos_los_libros():
            if titulo.lower() in libro.get_titulo().lower():
                resultados.append(libro)

        return resultados
    
    def buscar_libros_por_autor(self, autor):
        resultados = []

        for libro in self._obtener_todos_los_libros():
            if autor.lower() in libro.get_autor().lower():
                resultados.append(libro)

        return resultados
    
    def buscar_libros_por_categoria(self, categoria):
        resultados = []

        for libro in self._obtener_todos_los_libros():
            if categoria.lower() in libro.get_categoria().lower():
                resultados.append(libro)

        return resultados
    
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self._usuarios:
            return None

        usuario = self._usuarios[id_usuario]
        return usuario.get_libros_prestados()
    
    def listar_libros_disponibles(self):
        # Convierte los valores del diccionario en lista para mostrarlos más fácil.
        return list(self._libros_disponibles.values()) 