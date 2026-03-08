# Sistema de Gestión de Biblioteca Digital

## Descripción

Este proyecto consiste en el desarrollo de un sistema de gestión de biblioteca digital en Python, aplicando Programación Orientada a Objetos (POO) y una arquitectura por capas. El sistema permite administrar libros, usuarios, préstamos, devoluciones y búsquedas dentro del catálogo, separando correctamente los modelos, la lógica del negocio y el punto de entrada del programa.

La aplicación fue desarrollada en consola y organizada en carpetas para mantener una estructura clara, ordenada y fácil de mantener.

---

## Objetivo

Desarrollar un sistema de gestión de biblioteca digital que permita:

- Registrar libros en el catálogo.
- Registrar usuarios en la biblioteca.
- Realizar préstamos y devoluciones.
- Buscar libros por título, autor o categoría.
- Listar los libros prestados de un usuario.
- Aplicar correctamente colecciones en Python y separación por capas.

---

## Estructura del proyecto

```text
biblioteca_app/
│
├── modelos/
│   ├── libro.py
│   └── usuario.py
│
├── servicios/
│   └── biblioteca_servicio.py
│
└── main.py
