## LABORATORIO: FIGURA GEOMETRICA
# from FiguraGeometrica import FiguraGeometrica
# from Color import Color
#
#
# class Rectangulo(FiguraGeometrica, Color):
#     def __init__(self, ancho, alto, color):
#         FiguraGeometrica.__init__(self, ancho, alto)
#         Color.__init__(self, color)
#
#     def calcular_area(self):
#         return self.ancho * self.alto
#
#     def __str__(self):
#         # Cuando es herencia multiple y se utiliza el nombre de la clase para acceder a los metodos
#         # Es necesario indicar siempre el self para hacer referencia a este objeto
#         return f'Rectangulo[{FiguraGeometrica.__str__(self)} {Color.__str__(self)}]'


# LABORATORIO: FIGURA GEOMETRICA SOLUCION UBALDO
# from Color import Color
# from FiguraGeometrica import FiguraGeometrica
#
#
# class Rectangulo(FiguraGeometrica, Color):
#     def __init__(self, ancho, alto, color):
#         FiguraGeometrica.__init__(self, ancho, alto)
#         Color.__init__(self, color)
#
#     def calcular_area(self):
#         return self.alto * self.ancho
#
#     def __str__(self):
#         return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


# CLASE 71 CLASES ABSTRACTAS EN PYTHON
# from Color import Color
# from FiguraGeometrica import FiguraGeometrica
#
#
# class Rectangulo(FiguraGeometrica, Color):
#     def __init__(self, ancho, alto, color):
#         FiguraGeometrica.__init__(self, ancho, alto)
#         Color.__init__(self, color)
#
#     def calcular_area(self):
#         return self.alto * self.ancho
#
#     def __str__(self):
#         return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'