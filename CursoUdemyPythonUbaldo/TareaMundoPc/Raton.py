from DispositivoEntrada import DispositivoEntrada as dis


class Raton(dis):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        Raton.contadorRatones += 1
        self.__idRaton = Raton.contadorRatones

    @property
    def idRaton(self):
        return self.__idRaton

    def __str__(self):
        return f'\n\t\tRaton: Id: {self.__idRaton}, {super().__str__()}'


if __name__ == '__main__':
    r = Raton('usb', 'hp')
    print(r)