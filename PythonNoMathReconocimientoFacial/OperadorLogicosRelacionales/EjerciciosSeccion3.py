# Ejercicio 1
# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))
# resultado =  ((c + 5) * (pow(b, 2) - 3 * a * c)* pow(a, 2)) / (4 * a)
# print(f'El resultado es: {resultado}')

# Ejercicio 2
# a = input("a: ")
# b = input("b: ")
# a,b = b, a
# print(f'El nuevo valor de a es: {a}')
# print(f'El nuevo valor de b es: {b}')

# Ejercicio 3
# from math import pi 
# radio = float(input("Por favor ingrese el radio: "))
# area = pi * radio**2
# longitud = 2*pi*radio

# print(f'El area es: {area:.1f}')
# print(f'La longitud es: {longitud:.1f}')

# Ejercicio 4
'''
Obtener el precio final que se tiene que pagar si se aplica el 36% de descuento
del total de la compra
'''
compra = float(input("Ingrese el valor de la compra: "))
compra -= compra * 0.36
print(f'El valor a pagar es: {compra:.2f}')