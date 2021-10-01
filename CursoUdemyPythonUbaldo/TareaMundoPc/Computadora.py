from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor


class Computadora(Monitor, Teclado, Raton):
    contadorComputadoras = 0

    def __init__(self, tipoEntradaRaton, tipoEntradaTeclado,
                 marcaRaton, marcaTeclado, marcaMonitor, tamano):
        Raton.__init__(self, tipoEntradaRaton, marcaRaton)
        Teclado.__init__(self, tipoEntradaTeclado, marcaTeclado)
        Monitor.__init__(self, marcaMonitor, tamano)
        Computadora.contadorComputadoras += 1
        self.__idComputadora = Computadora.contadorComputadoras

    @property
    def idComputadora(self):
        return self.__idComputadora

    def __str__(self):
        return f'\n\tComputadora: Id: {self.idComputadora} {Monitor.__str__(self)}, {Raton.__str__(self)}, {Teclado.__str__(self)}'


if __name__ == '__main__':
    c = Computadora('usb', 'usb', 'hp', 'hp','hp', '14 pulgadas')
    print(c)