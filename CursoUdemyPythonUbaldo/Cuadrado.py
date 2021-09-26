# CLASE 68 HERENCIA MULTIPLE EN PYTHON PARTE 2
# from FiguraGeometrica import FiguraGeometrica
# from Color import Color
#
# Para trabajar con herencia multiple se deberan separar las clases con comas y si importara el ornde
# class Cuadrado(FiguraGeometrica, Color):
#     def __init__(self, lado, color):
#         # super().__init__(lado, lado) # En este caso se llamara el contructor de la clase padre que digamos primero en los parentesis de la declaracion
#         # Ademas este se puede utilizar porque diferencia entre la cantidad de argumentos de los init de las clases
#         # padre Sin embargo, esto se puede tornar confuso por ende vamos a ver la siguiente forma
#
#         FiguraGeometrica.__init__(self, lado, lado) # En este caso se utiliza el nombre de la clase luego el init y se debe de pasar el parametro de self
#         # Ejemplo Clase.__init__(self, argumentos)
#         Color.__init__(self, color)
#
#     def calcular_area(self):
#         return self.alto * self.ancho

# CLASE 69 HERENCIA MULTIPLE EN PYTHON PARTE 3
# from FiguraGeometrica import FiguraGeometrica
# from Color import Color
#
#
# class Cuadrado(FiguraGeometrica, Color):
#     def __init__(self, lado, color):
#         # super().__init__(lado, lado) # En este caso se llamara el contructor de la clase padre que digamos primero en los parentesis de la declaracion
#         # Ademas este se puede utilizar porque diferencia entre la cantidad de argumentos de los init de las clases
#         # padre Sin embargo, esto se puede tornar confuso por ende vamos a ver la siguiente forma
#
#         FiguraGeometrica.__init__(self, lado, lado) # En este caso se utiliza el nombre de la clase luego el init y se debe de pasar el parametro de self
#         # Ejemplo Clase.__init__(self, argumentos)
#         Color.__init__(self, color)
#
#     def calcular_area(self):
#         return self.alto * self.ancho


# CLASE 70 METODO MRO - METHOD RESOLUTION ORDER EN PYTHON
# from FiguraGeometrica import FiguraGeometrica
# from Color import Color
#
#
# class Cuadrado(Color, FiguraGeometrica):
#     def __init__(self, lado, color):
#         # super().__init__(lado, lado) # En este caso se llamara el contructor de la clase padre que digamos primero en los parentesis de la declaracion
#         # Ademas este se puede utilizar porque diferencia entre la cantidad de argumentos de los init de las clases
#         # padre Sin embargo, esto se puede tornar confuso por ende vamos a ver la siguiente forma
#
#         FiguraGeometrica.__init__(self, lado, lado) # En este caso se utiliza el nombre de la clase luego el init y se debe de pasar el parametro de self
#         # Ejemplo Clase.__init__(self, argumentos)
#         Color.__init__(self, color)
#
#     def calcular_area(self):
#         return self.alto * self.ancho


# LABORATORIO: FIGURA GEOMETRICA
# from FiguraGeometrica import FiguraGeometrica
# from Color import Color
#
#
# class Cuadrado(Color, FiguraGeometrica):
#     def __init__(self, lado, color):
#         # super().__init__(lado, lado) # En este caso se llamara el contructor de la clase padre que digamos primero en los parentesis de la declaracion
#         # Ademas este se puede utilizar porque diferencia entre la cantidad de argumentos de los init de las clases
#         # padre Sin embargo, esto se puede tornar confuso por ende vamos a ver la siguiente forma
#
#         FiguraGeometrica.__init__(self, lado, lado)  # En este caso se utiliza el nombre de la clase luego el init y se debe de pasar el parametro de self
#         # Ejemplo Clase.__init__(self, argumentos)
#         Color.__init__(self, color)
#
#     def calcular_area(self):
#         return self.alto * self.ancho
#
#     def __str__(self):
#         # Cuando es herencia multiple y se utiliza el nombre de la clase para acceder a los metodos
#         # Es necesario indicar siempre el self para hacer referencia a este objeto
#         return f'Cuadrado[Area: {self.calcular_area()}, {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}]'


# LABORATORIO: FIGURA GEOMETRICA SOLUCION UBALDO
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

