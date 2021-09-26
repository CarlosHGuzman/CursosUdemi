# CLASE 72 VARIABLES DE CLASE EN PYTHON
# class MiClase:
#
#     # Esta variable de clase se podra compartir entre todos los objetos que se creen
#     # A partir de esta clase
#     variable_clase = 'Valor variable clase'
#
#     def __init__(self, variable_instancia):
#         self._variable_instancia = variable_instancia
#
#     @property
#     def variable_instancia(self):
#         return self._variable_instancia
#
#     @variable_instancia.setter
#     def variable_instancia(self, variable_instancia):
#         self._variable_instancia = variable_instancia
#
#
# print(MiClase.variable_clase)
# miClase = MiClase("Valor variable instancia")
# print(miClase.variable_instancia)
# print(miClase.variable_clase)
#
# miClase2 = MiClase("Otro valor de instancia")
# print(miClase2.variable_instancia)
# print(miClase2.variable_clase)


# CLASE 73 CREACION DE VARIABLES DE CLASE AL VUELO EN PYTHON
# class MiClase:
#
#     # Esta variable de clase se podra compartir entre todos los objetos que se creen
#     # A partir de esta clase
#     variable_clase = 'Valor variable clase'
#
#     def __init__(self, variable_instancia):
#         self._variable_instancia = variable_instancia
#
#     @property
#     def variable_instancia(self):
#         return self._variable_instancia
#
#     @variable_instancia.setter
#     def variable_instancia(self, variable_instancia):
#         self._variable_instancia = variable_instancia
#
#
# print(MiClase.variable_clase)
# miClase = MiClase("Valor variable instancia")
# print(miClase.variable_instancia)
# print(miClase.variable_clase)
#
# # Esto quiere decir que podemos crear atributos de clase en cualquier momento
# # Sin embargo cuando se crea por fuera de la clase, el IDE no nos recomendara la variable de clase
# # pero se puede utilizar
# MiClase.variable_clase2 = 'Valor variable clase 2'
#
# miClase2 = MiClase("Otro valor de instancia")
# print(miClase2.variable_instancia)
# print(miClase2.variable_clase)
# print(miClase2.variable_clase2)


# CLASE 74 METODOS ESTATICOS EN PYTHON
# class MiClase:
#
#     # Esta variable de clase se podra compartir entre todos los objetos que se creen
#     # A partir de esta clase
#     variable_clase = 'Valor variable clase'
#
#     def __init__(self, variable_instancia):
#         self._variable_instancia = variable_instancia
#
#     @property
#     def variable_instancia(self):
#         return self._variable_instancia
#
#     @variable_instancia.setter
#     def variable_instancia(self, variable_instancia):
#         self._variable_instancia = variable_instancia
#
#     # No se puede acceder al metodo self y a ningun tipo de atributo o metodo puesto que no se han instanciado
#     @staticmethod
#     def metodo_estatico():
#         print(MiClase.variable_clase)
#         #print(variable_clase ) # No se puede acceder a la variable de clase si no lo antecede el nombre de la clase
#
#
# MiClase.metodo_estatico()


# CLASE 75 METODOS DE CLASE EN PYTHON
# class MiClase:
#     # Esta variable de clase se podra compartir entre todos los objetos que se creen
#     # A partir de esta clase
#     variable_clase = 'Valor variable clase'
#
#     def __init__(self, variable_instancia):
#         self._variable_instancia = variable_instancia
#
#     @property
#     def variable_instancia(self):
#         return self._variable_instancia
#
#     @variable_instancia.setter
#     def variable_instancia(self, variable_instancia):
#         self._variable_instancia = variable_instancia
#
#     # No se puede acceder al metodo self y a ningun tipo de atributo o metodo puesto que no se han instanciado
#     @staticmethod
#     def metodo_estatico():
#         print(MiClase.variable_clase)
#         # print(variable_clase ) # No se puede acceder a la variable de clase si no lo antecede el nombre de la clase
#
#     # cls = class pero puede ser cualquier otro nombre
#     # Este puede acceder a los atributos de la clase
#     @classmethod
#     def metodo_clase(cls):
#         print(cls.variable_clase)
#         print(cls.metodo_estatico())
#
#
# MiClase.metodo_clase()


# CLASE 76 CONTEXTO ESTATICO Y DINAMICO EN PYTHON
# class MiClase:
#     # Esta variable de clase se podra compartir entre todos los objetos que se creen
#     # A partir de esta clase
#     variable_clase = 'Valor variable clase'
#
#     def __init__(self, variable_instancia):
#         self._variable_instancia = variable_instancia
#
#     @property
#     def variable_instancia(self):
#         return self._variable_instancia
#
#     @variable_instancia.setter
#     def variable_instancia(self, variable_instancia):
#         self._variable_instancia = variable_instancia
#
#     # No se puede acceder al metodo self y a ningun tipo de atributo o metodo puesto que no se han instanciado
#     @staticmethod
#     def metodo_estatico():
#         print(MiClase.variable_clase)
#         # print(variable_clase ) # No se puede acceder a la variable de clase si no lo antecede el nombre de la clase
#
#     # cls = class pero puede ser cualquier otro nombre
#     # Este puede acceder a los atributos de la clase
#     @classmethod
#     def metodo_clase(cls):
#         print(cls.variable_clase)
#         cls.metodo_estatico()
#
#     def metodo_instancia(self):
#         self.metodo_clase()
#         self.metodo_estatico()
#         print(self.variable_clase)
#         print(self.variable_instancia)
#
#
# # El contexto estatico(clase) no puede acceder al contexto dinamico que son solo los objetos
# # pero el contexto dinamico si puede acceder al metodo estatico
# MiClase.metodo_clase()
# miObjeto1 = MiClase("VAlor Variable_instancia")
# miObjeto1.metodo_clase()
# miObjeto1.metodo_instancia()
