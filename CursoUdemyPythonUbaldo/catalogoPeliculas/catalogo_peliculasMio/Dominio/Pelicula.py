class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return f'Pelicula: {self.nombre}'


if __name__ == '__main__':
    nombre = input("Por favor ingrese el nombre de la pelicula: ")
    pelicula1 = Pelicula('nombre')
    print(pelicula1)