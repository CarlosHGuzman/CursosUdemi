class ManejoArchivos:
    # los metodos exit y open ya estan definidos en la clase padre object
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    # traceback(traza) = toda la lista de errores si es que ocurrió alguno
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        # Se deben agregar estos parametros para cumplir con la firma del metodo
        # La cual indica que debemos agregar esos parametros, para evitar un error
        print('Cerramos el recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close()