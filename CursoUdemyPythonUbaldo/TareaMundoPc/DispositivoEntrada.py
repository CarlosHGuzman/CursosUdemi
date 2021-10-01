class DispositivoEntrada:
    def __init__(self, tipoEntrada: str, marca: str):
        if self.validar_datos(tipoEntrada):
            self.__tipoEntrada = tipoEntrada
        else:
            print("No se puede agregar tipo de dato invalido")
        if self.validar_datos(marca):
            self.__marca = marca
        else:
            print("No se puede agregar tipo de dato invalido")

    @property
    def tipoEntrada(self):
        return self.__tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self.__tipoEntrada = tipoEntrada

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def validar_datos(self, dato):
        return True if str == type(dato) else False

    def __str__(self):
        return f'tipo de Entrada: {self.tipoEntrada}, marca: {self.marca}'


if __name__ == '__main__':
    d = DispositivoEntrada('usb', 'hp')
    print(d)
