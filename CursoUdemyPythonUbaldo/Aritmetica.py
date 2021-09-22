# CLASE 55 EJERCICIO CLASE ARITMETICA
# class Aritmetica:
#     """
#     Clase Aritmetica para realizar las operaciones de sumar, restar, etc
#     """
#     def __init__(self, operandoA, operandoB):
#         self.operandoA = operandoA
#         self.operandoB = operandoB
#
#     def sumar(self):
#         return self.operandoA + self.operandoB
#
#
# aritmetica1 = Aritmetica(5, 3)
# print(aritmetica1.sumar())


# CLASE 56 EJERCICIO CLASE ARITMETICA
# class Aritmetica:
#     """
#     Clase Aritmetica para realizar las operaciones de sumar, restar, etc
#     """
#     def __init__(self, operandoA, operandoB):
#         self.operandoA = operandoA
#         self.operandoB = operandoB
#
#     def sumar(self):
#         return self.operandoA + self.operandoB
#
#     def restar(self):
#         return self.operandoA - self.operandoB
#
#     def multiplicar(self):
#         return self.operandoA * self.operandoB
#
#     def division(self):
#         return (self.operandoA / self.operandoB)
#
#
# aritmetica1 = Aritmetica(5, 3)
# print(f'Suma: {aritmetica1.sumar()}')
# print(f'Restar: {aritmetica1.restar()}')
# print(f"Multiplicacion: {aritmetica1.multiplicar()}")
# print(f"Division: {aritmetica1.division():.2f}") #solo se puede utilizar ":2.f" para redondear el numero cuando se utiliza el formato f
# print(aritmetica1.division())


#TAREA LABORATORIO RECTANGULO
# class Rectangulo:
#     def __init__(self, altura, base):
#         self.base = base
#         self.altura = altura
#
#     def calcular_area(self):
#         return self.base * self.altura
#
# altura = float(input("Ingrese la altura del rectangulo: "))
# base = float(input("Ingrese la base del rectangulo: "))
#
# rectangulo1 = Rectangulo(altura, base)
# print(rectangulo1.calcular_area())


# SOLUCION TAREA Ubaldo
# class Rectangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
#
#     def calcular_area(self):
#         return self.base * self.altura
#
# base = int(input('Proporciona la base: '))
# altura = int(input('Proporciona la altura: '))
#
# rectangulo1 = Rectangulo(base, altura)
# print(f'Area rectangulo: {rectangulo1.calcular_area()}')
#
# base = int(input('Proporciona la base: '))
# altura = int(input('Proporciona la altura: '))
#
# rectangulo2 = Rectangulo(base, altura)
# print(f'Area rectangulo: {rectangulo2.calcular_area()}')


#TAREA LABORATORIO CUBO
# class Cubo:
#     def __init__(self, ancho, profundidad, altura):
#         self.ancho = ancho
#         self.profundidad = profundidad
#         self.altura = altura
#
#     def calcular_volumen(self):
#         return self.ancho * self.profundidad * self.altura
# print("------------------CUBO-------------------")
# ancho = float(input("Por favor ingrese el ancho del cubo: "))
# profundidad = float(input("Por favor ingrese la profundidad del cubo: "))
# altura = float(input("Por favor ingrese la altura del cubo: "))
#
# cubo1 = Cubo(ancho, profundidad, altura)
# print(f'El volumen del cubo es: {cubo1.calcular_volumen():.2f}')


#SOLUCION TAREA Ubaldo
# class Cubo:
#     def __init__(self, ancho, alto, profundo):
#         self.ancho = ancho
#         self.alto = alto
#         self.produndo = profundo
#
#     def calcular_volumen(self):
#         return self.ancho * self.alto * self.produndo
#
# ancho = int(input('Proporciona el ancho: '))
# alto = int(input('Proporciona el alto: '))
# profundo = int(input('Proporciona lo profundo: '))
#
# cubo1 = Cubo(ancho, alto, profundo)
# print(f'Volumen cubo: {cubo1.calcular_volumen()}')