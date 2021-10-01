from DispositivoEntrada import DispositivoEntrada as dis


class Teclado(dis):
    contadorTeclados = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        Teclado.contadorTeclados += 1
        self.__idTeclado = Teclado.contadorTeclados

    @property
    def idTeclado(self):
        return self.__idTeclado

    def __str__(self):
        return f'\n\t\tTeclado: Id: {self.idTeclado}, {super().__str__()}'


if __name__ == '__main__':
    t = Teclado('usb', 'hp')
    print(t)