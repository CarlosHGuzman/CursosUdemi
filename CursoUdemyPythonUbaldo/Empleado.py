# CLASE 84 POLIMOFRISMO EN PYTHON - PARTE 1
# class Empleado:
#     def __init__(self, nombre, sueldo):
#         self.__nombre = nombre
#         self.__sueldo = sueldo
#
#     @property
#     def nombre(self):
#         return self.__nombre
#
#     @nombre.setter
#     def nombre(self, nombre):
#         self.__nombre = nombre
#
#     @property
#     def sueldo(self):
#         return self.__sueldo
#
#     @sueldo.setter
#     def sueldo(self, sueldo):
#         self.__sueldo = sueldo
#
#     def __str__(self):
#         return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'


# CLASE 85 POLIMOFRISMO EN PYTHON - PARTE 2
# class Empleado:
#     def __init__(self, nombre, sueldo):
#         self.__nombre = nombre
#         self.__sueldo = sueldo
#
#     @property
#     def nombre(self):
#         return self.__nombre
#
#     @nombre.setter
#     def nombre(self, nombre):
#         self.__nombre = nombre
#
#     @property
#     def sueldo(self):
#         return self.__sueldo
#
#     @sueldo.setter
#     def sueldo(self, sueldo):
#         self.__sueldo = sueldo
#
#     def __str__(self):
#         return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'
#
#     def mostrar_detalles(self):
#         return self.__str__()


# CLASE 86 METODO ISINSTANCE Y POLIMORFISMO EN PYTHON AND METODO DEBUG
class Empleado:
    def __init__(self, nombre, sueldo):
        self.__nombre = nombre
        self.__sueldo = sueldo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self.__sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()
