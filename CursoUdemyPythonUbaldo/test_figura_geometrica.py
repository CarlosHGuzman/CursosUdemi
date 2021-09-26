# CLASE 69 HERENCIA MULTIPLE EN PYTHON PARTE 3
# from Cuadrado import Cuadrado
#
# print("Bienvenido al programa de Cubo".center(50, '='))
# lado = float(input("Ingrese el valor del lado: "))
# color = str(input("Ingrese el color del cubo: "))
# cuadrado1 = Cuadrado(lado, color)
# # print(cuadrado1.ancho)
# # print(cuadrado1.alto)
# # print(cuadrado1.color)
# print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')


# CLASE 70 METODO MRO - METHOD RESOLUTION ORDER EN PYTHON
# Se utiliza para saber en que orden se van a ejecutar las clases.
# from Cuadrado import Cuadrado
#
# print("Bienvenido al programa de Cubo".center(50, '='))
# lado = float(input("Ingrese el valor del lado: "))
# color = str(input("Ingrese el color del cubo: "))
# cuadrado1 = Cuadrado(lado, color)
# # print(cuadrado1.ancho)
# # print(cuadrado1.alto)
# # print(cuadrado1.color)
# print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')
# print(Cuadrado.mro())  # Esto tiene que ver con el orden en el que heredamos las clases en una clase
# # Es decir si heredamos (claase1, clase2) lo primero que imprimira es la clase actual
# # Luego imprimir la clase1 y por ultimo clase2


# LABORATORIO: FIGURA GEOMETRICA
# from Cuadrado import Cuadrado
# from Rectangulo import Rectangulo
#
# print('Creacion Objeto cuadrado'.center(50, '-'))
# cuadrado1 = Cuadrado(lado = -5, color = 'red')
# print(f"CalculoArea Cuadrado: {(cuadrado1.calcular_area())}")
# print(cuadrado1)
#
# print("Creacion Objeto retangulo".center(50, '-'))
# rectangulo1 = Rectangulo(ancho = 13, alto = 8, color = 'green')
# print(f'Cálculo área rectangulo: {rectangulo1.calcular_area()}')
# print(rectangulo1)


# LABORATORIO: FIGURA GEOMETRICA SOLUCION UBALDO
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación Objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación Objeto rectángulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho=9, alto=8, color='verde')
rectangulo1.ancho = 15
print(f'Cálculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)