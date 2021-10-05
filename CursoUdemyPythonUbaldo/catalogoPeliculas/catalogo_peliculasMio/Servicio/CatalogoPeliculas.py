from catalogoPeliculas.catalogo_peliculasMio.Dominio.Pelicula import Pelicula
import os


class CatalogoPeliculas(Pelicula):
    ruta_archivo = open('Peliculas.txt', 'a+', encoding='utf8')

    def __init__(self, nombre):
        super().__init__(nombre)

    @staticmethod
    def agregar_peliculas(pelicula):
        try:
            if isinstance(pelicula, Pelicula):
                CatalogoPeliculas.ruta_archivo.write(str(pelicula))
            else:
                print('No se pudo agregar la pelicula')
        except Exception as e:
            print(f"Ha ocurrido algo inesperado. {e}")

    @staticmethod
    def listar_peliculas():
        leer = ''
        for line in CatalogoPeliculas.ruta_archivo:
            leer += line
        return CatalogoPeliculas.ruta_archivo.read()

    @staticmethod
    def eliminar():
        os.remove(CatalogoPeliculas.ruta_archivo)
        print('Se ha eliminado el archivo'.center(50, '-'))


if __name__ == '__main__':
    pelicula1 = Pelicula('Titanic')
    pelicula2 = Pelicula('Pasion de gabilanes')
    catalogo1 = CatalogoPeliculas('tita')
    catalogo1.agregar_peliculas(pelicula1)
    print(catalogo1.listar_peliculas())
    catalogo1.agregar_peliculas(pelicula2)
    print(catalogo1.listar_peliculas())
