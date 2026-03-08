from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio

def mostrar_libros(libros):
    # Esta función se crea para no repetir el mismo bloque varias veces.
    if not libros:
        print("No hay libros para mostrar.")
    else:
        for libro in libros:
            print(libro)

def menu():
    # Aquí se crea el servicio principal del sistema.
    # main.py solo controla la interacción con el usuario.
    biblioteca = BibliotecaServicio()

    while True:
        print("\n--- BIBLIOTECA DIGITAL ---")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Eliminar usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros por título")
        print("8. Buscar libros por autor")
        print("9. Buscar libros por categoría")
        print("10. Listar libros prestados de un usuario")
        print("11. Listar libros disponibles")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            categoria = input("Categoría: ").strip()
            isbn = input("ISBN: ").strip()

            libro = Libro(titulo, autor, categoria, isbn)
            print(biblioteca.agregar_libro(libro))

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ").strip()
            print(biblioteca.eliminar_libro(isbn))

        elif opcion == "3":
            nombre = input("Nombre del usuario: ").strip()
            id_usuario = input("ID del usuario: ").strip()

            usuario = Usuario(nombre, id_usuario)
            print(biblioteca.registrar_usuario(usuario))

        elif opcion == "4":
            id_usuario = input("ID del usuario a eliminar: ").strip()
            print(biblioteca.eliminar_usuario(id_usuario))

        elif opcion == "5":
            isbn = input("ISBN del libro a prestar: ").strip()
            id_usuario = input("ID del usuario: ").strip()
            print(biblioteca.prestar_libro(isbn, id_usuario))

        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ").strip()
            id_usuario = input("ID del usuario: ").strip()
            print(biblioteca.devolver_libro(isbn, id_usuario))

        elif opcion == "7":
            titulo = input("Ingrese el título a buscar: ").strip()
            resultados = biblioteca.buscar_libros_por_titulo(titulo)
            mostrar_libros(resultados)

        elif opcion == "8":
            autor = input("Ingrese el autor a buscar: ").strip()
            resultados = biblioteca.buscar_libros_por_autor(autor)
            mostrar_libros(resultados)

        elif opcion == "9":
            categoria = input("Ingrese la categoría a buscar: ").strip()
            resultados = biblioteca.buscar_libros_por_categoria(categoria)
            mostrar_libros(resultados)

        elif opcion == "10":
            id_usuario = input("ID del usuario: ").strip()
            resultados = biblioteca.listar_libros_prestados(id_usuario)

            if resultados is None:
                print("Usuario no encontrado.")
            else:
                mostrar_libros(resultados)

        elif opcion == "11":
            resultados = biblioteca.listar_libros_disponibles()
            mostrar_libros(resultados)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

