class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamano):
        Monitor.contadorMonitores += 1
        self.__idMonitor = Monitor.contadorMonitores
        self.__marca = marca
        self.__tamano = tamano

    @property
    def idMonitor(self):
        return self.__idMonitor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def tamano(self):
        return self.__tamano

    @tamano.setter
    def tamano(self, tamano):
        self.__tamano = tamano

    def __str__(self):
        return f'\n\t\tMonitor: Id: {self.idMonitor}, Marca: {self.marca}. Tamaño: {self.tamano}'


if __name__ == '__main__':
    m = Monitor('hp', '14 pulgadas')
    print(m)
