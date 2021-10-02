# CLASE 67 HERENCIA MULTIPLE EN PYTHON
# class FiguraGeometrica:
#     def __init__(self, ancho, alto):
#         self._ancho = ancho
#         self._alto = alto
#
#     @property
#     def ancho(self):
#         return self._ancho
#
#     @ancho.setter
#     def ancho(self, ancho):
#         self._ancho = ancho
#
#     @property
#     def alto(self):
#         return self._alto
#
#     @alto.setter
#     def alto(self, alto):
#         self._alto = alto
#
#     def __str__(self):
#         return f'Figura Geometrica[ancho: {self._ancho} alto: {self._alto}]'


# CLASE 68 HERENCIA MULTIPLE EN PYTHON PARTE 2
# class FiguraGeometrica:
#     def __init__(self, ancho, alto):
#         self._ancho = ancho
#         self._alto = alto
#
#     @property
#     def ancho(self):
#         return self._ancho
#
#     @ancho.setter
#     def ancho(self, ancho):
#         self._ancho = ancho
#
#     @property
#     def alto(self):
#         return self._alto
#
#     @alto.setter
#     def alto(self, alto):
#         self._alto = alto
#
#     def __str__(self):
#         return f'Figura Geometrica[ancho: {self._ancho} alto: {self._alto}]'
#

# CLASE 69 HERENCIA MULTIPLE EN PYTHON PARTE 3
# class FiguraGeometrica:
#     def __init__(self, ancho, alto):
#         self._ancho = ancho
#         self._alto = alto
#
#     @property
#     def ancho(self):
#         return self._ancho
#
#     @ancho.setter
#     def ancho(self, ancho):
#         self._ancho = ancho
#
#     @property
#     def alto(self):
#         return self._alto
#
#     @alto.setter
#     def alto(self, alto):
#         self._alto = alto
#
#     def __str__(self):
#         return f'Figura Geometrica[ancho: {self._ancho} alto: {self._alto}]'


# CLASE 70 METODO MRO - METHOD RESOLUTION ORDER EN PYTHON
# class FiguraGeometrica:
#     def __init__(self, ancho, alto):
#         self._ancho = ancho
#         self._alto = alto
#
#     @property
#     def ancho(self):
#         return self._ancho
#
#     @ancho.setter
#     def ancho(self, ancho):
#         self._ancho = ancho
#
#     @property
#     def alto(self):
#         return self._alto
#
#     @alto.setter
#     def alto(self, alto):
#         self._alto = alto
#
#     def __str__(self):
#         return f'Figura Geometrica[ancho: {self._ancho} alto: {self._alto}]'


# LABORATORIO: FIGURA GEOMETRICA
# class FiguraGeometrica:
#     def __init__(self, ancho, alto):
#         if self.__validar_valor(ancho):
#             self._ancho = ancho
#         else:
#             self._ancho = 0
#         if self.__validar_valor(alto):
#             self._alto = alto
#         else:
#             self._alto = 0
#
#     @property # Decorador
#     def ancho(self):
#         return self._ancho
#
#     @ancho.setter
#     def ancho(self, ancho):
#         self._ancho = ancho
#
#     @property
#     def alto(self):
#         return self._alto
#
#     @alto.setter
#     def alto(self, alto):
#         self._alto = alto
#
#     def __validar_valor(self, valor):
#         return True if 0 < valor < 10 else False
#
#     def __str__(self):
#         return f'Figura Geometrica[ancho: {self._ancho} alto: {self._alto}]'


# LABORATORIO: FIGURA GEOMETRICA SOLUCION UBALDO
# class FiguraGeometrica:
#     def __init__(self, ancho, alto):
#         if self._validar_valor(ancho):
#             self._ancho = ancho
#         else:
#             self._ancho = 0
#             print(f'Valor erroneo ancho: {ancho}')
#         if self._validar_valor(alto):
#             self._alto = alto
#         else:
#             self._alto = 0
#             print(f'Valor erroneo alto: {alto}')
#
#     @property
#     def ancho(self):
#         return self._ancho
#
#     @ancho.setter
#     def ancho(self, ancho):
#         if self._validar_valor(ancho):
#             self._ancho = ancho
#         else:
#             print(f'Valor erroneo ancho: {ancho}')
#
#     @property
#     def alto(self):
#         return self._alto
#
#     @alto.setter
#     def alto(self, alto):
#         if self._validar_valor(alto):
#             self._alto = alto
#         else:
#             print(f'Valor erroneo alto: {alto}')
#
#     def __str__(self):
#         return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self.alto} ]'
#
#     def _validar_valor(self, valor):
#         return True if 0 < valor < 10 else False


# CLASE 71 CLASES ABSTRACTAS EN PYTHON
# ABC = Abstract Base Class para importar una clase se separan por comas
# from abc import ABC, abstractmethod
#
#
# class FiguraGeometrica(ABC):
#     def __init__(self, ancho, alto):
#         if self._validar_valor(ancho):
#             self._ancho = ancho
#         else:
#             self._ancho = 0
#             print(f'Valor erroneo ancho: {ancho}')
#         if self._validar_valor(alto):
#             self._alto = alto
#         else:
#             self._alto = 0
#             print(f'Valor erroneo alto: {alto}')
#
#     @property
#     def ancho(self):
#         return self._ancho
#
#     @property
#     def alto(self):
#         return self._alto
#
#     @abstractmethod
#     def calcular_area(self):
#         pass
#
#     def __str__(self):
#         return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self.alto} ]'
#
#     def _validar_valor(self, valor):
#         return True if 0 < valor < 10 else False
