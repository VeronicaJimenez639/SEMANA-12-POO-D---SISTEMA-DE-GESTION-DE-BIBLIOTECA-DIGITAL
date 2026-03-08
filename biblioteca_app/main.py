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