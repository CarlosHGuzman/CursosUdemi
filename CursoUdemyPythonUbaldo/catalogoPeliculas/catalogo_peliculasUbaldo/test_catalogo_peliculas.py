from catalogoPeliculas.catalogo_peliculasUbaldo.dominio.Pelicula import Pelicula
from catalogoPeliculas.catalogo_peliculasUbaldo.servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None

while opcion != 4:
    try:
        print('Opciones: ')
        opcion = int(input('''
1. Agregar Película
2. Listar Películas
3. Eliminar catálogo películas
4. Salir
Ingrese la opcion(1-4): '''))
        if opcion == 1:
            nombre_pelicula = input('Por favor proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
        else:
            print("Opcion invalida")
    except Exception as e:
        print(f"Ocurrio un erro {e}")
        opcion = None
else:
    print("Salimos del programa....")
