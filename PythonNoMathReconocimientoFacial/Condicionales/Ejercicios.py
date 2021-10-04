'''
Ejercicio 1
Crear un programa que pida 2 numero y obtenga como resultado 
cual de ello ses par o si ambos lo son
'''
# numero1 = int(input("Por favor ingrese un numero: "))
# numero2 = int(input("Por favor ingrese un segundo numero: "))

# if numero1 % 2 == 0 and numero2 % 2 == 0:
#     print("Ambos son pares")
# elif numero1 % 2 == 0 and numero2 % 2 != 0:
#     print(f'{numero1} es un numero par')
# elif numero1 % 2 != 0 and numero2 % 2 == 0:
#     print(f'{numero2} es un numero par')
# else: 
#     print("Los dos numero son impares")

'''
Ejercicio 2
Crear un programa que pida 3 números y determine cual es el mayor
'''
# numero1 = int(input("Por favor ingrese el numero: "))
# numero2 = int(input("Por favor ingrese un numero: "))
# numero3 = int(input("Por favor ingrese un numero: "))

# if numero1 >= numero2 and numero1 >= numero3:
#     print(f'El numero mayor es: {numero1}')
# elif numero2 >= numero3: 
#     print(f'El numero mayor es: {numero2}')
# else:
#     print(f'El numero mayor es: {numero3}')

'''
Ejercicio 3
Crea un programa que compare dos nombres, y verificar si hay 
coincidencia o no, si es que ambos nombres comiezna con la misma letra 
o si terminan con la misma letra.
'''
# nombre1 = input("Ingrese un nombre 1: ")
# nombre2 = input("Ingrese un nombre 2: ")
# if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
#     print("Si hay coincidencia")
# else: 
#     print("No hay coincidencia")

'''
Ejercicio 4
Crear un programa que simule un cajero automatico con un saldo
inicial de $ 2000, con el siguiente menu:

1. Ingreso de dinero
2. Retirar dinero
3. Mostrar dinero
4. Salir
'''
saldo_inicial = 2000
print("""
1. Ingreso de dinero
2. Retiro de dinero
3. Mostrar dinero
4. Salir 
""")
seleccion = int(input("Elija una opcion: "))
if seleccion == 1:
    ingresoDineroUsuario = float(input("Dinero a ingresar: "))
    saldo_inicial += ingresoDineroUsuario
    print(f'Nuevo saldo en la cuenta: {saldo_inicial}')
elif seleccion == 2:
    salidaDineroUsuario = float(input("Dinero de salida: "))
    if salidaDineroUsuario > saldo_inicial:
        print("Saldo insuficiente")
    elif salidaDineroUsuario < 0:
        print("Ingrese un salida positiva")
    else:
        saldo_inicial -= salidaDineroUsuario
        print(f'Nuevo saldo disponible: {saldo_inicial}')
elif seleccion == 3:
    print(f'Saldo disponible: {saldo_inicial}')
elif seleccion == 4:
    print("Fin del programa")
else:
    print("Error de entrada de datos(opcion invalida)")