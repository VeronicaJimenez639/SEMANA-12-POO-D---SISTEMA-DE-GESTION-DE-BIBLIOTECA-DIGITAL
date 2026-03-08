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