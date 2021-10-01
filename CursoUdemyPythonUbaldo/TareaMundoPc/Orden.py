from Computadora import Computadora


class Orden:
    contadorOrdenes = 0

    def __init__(self):
        Orden.contadorOrdenes += 1
        self.__idOrden = Orden.contadorOrdenes
        self.__listaComputadoras = list()

    @property
    def idOrden(self):
        return self.__idOrden

    @property
    def listaComputadoras(self):
        return self.__listaComputadoras

    def agregarComputadora(self, computadora):
        if isinstance(computadora, Computadora):
            self.listaComputadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for i in self.listaComputadoras:
            computadoras_str += i.__str__()
        return f'Orden: id: {self.idOrden} Computadoras: {computadoras_str}'
