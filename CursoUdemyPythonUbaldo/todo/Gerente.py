# CLASE 85 POLIMOFRISMO EN PYTHON - PARTE 1
# from Empleado import Empleado
#
#
# class Gerente(Empleado):
#     def __init__(self,nombre, sueldo, departamento):
#         Empleado.__init__(self, nombre, sueldo)
#         self.__departamento = departamento
#
#     @property
#     def departamento(self):
#         return self.__departamento
#     @departamento.setter
#     def departamento(self, departamento):
#         self.__departamento = departamento
#
#     def __str__(self):
#         return f'Gerente[Dapartamento: {self.departamento},[ {super.__str__(self)}]]'


# CLASE 86 POLIMOFRISMO EN PYTHON - PARTE 2
# from Empleado import Empleado
#
#
# class Gerente(Empleado):
#     def __init__(self, nombre, sueldo, departamento):
#         Empleado.__init__(self, nombre, sueldo)
#         self.__departamento = departamento
#
#     @property
#     def departamento(self):
#         return self.__departamento
#
#     @departamento.setter
#     def departamento(self, departamento):
#         self.__departamento = departamento
#
#     def __str__(self):
#         return f'Gerente[Dapartamento: {self.departamento},[ {super().__str__()}]]'
#
#     # def mostrar_detalles(self):
#     #     return self.__str__()


# CLASE 87 METODO ISINSTANCE Y POLIMORFISMO EN PYTHON AND METODO DEBUG
from Empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        Empleado.__init__(self, nombre, sueldo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    def __str__(self):
        return f'Gerente[Dapartamento: {self.departamento},[ {super().__str__()}]]'

    # def mostrar_detalles(self):
    #     return self.__str__()
