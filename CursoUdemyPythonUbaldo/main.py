# Clase 1 HolaMundoPython
# print("Hola Mundo con Python")

# Clase 2 VariablesPython
# miVariable = 2
# print( miVariable )
# print( miVariable )
# print( miVariable )

# miVariable = 10
# print( miVariable )

# CLASE 3 VARIABLES PYTHON PARTE 2
# x = 10
# y = 2
# z = x + y
# print(x)
# print(y)
# print(z)

# CLASE 4 DIRECCION DE MEMORIA VARIABLES
# x = 10
# y = 2
# z = x + y
# print(x)
# print(y)
# print(z)
# print(id(x))
# print(id(y))
# print(id(z))

# CLASE 5 TIPOS DE DATOS
# x = False
# print(x)
# print(type(x))

# CLASE 6 TIPOS STRING
# Cadena (String)
# miGrupoFavorito = "Metallica"
# comentario = "The Best Rock Band"
# print("Mi grupo favorito es: " + miGrupoFavorito + " " + comentario)

# CLASE 7 ENTRADA CON LA FUNCION INPUT
# Función input para procesar la entrada del usuario
# resultado = input("Escribe un mensaje: ")
# print("Valor proporcionado:",resultado)
# print("Fin del programa")

# CLASE 8 CONVERSION FUNCION INPUT A NUMVER
# Función input para procesar la entrada del usuario
# numero1 = int(input("Escribe el primer número: "))
# numero2 = int(input("Escribe el segundo número: "))
# resultado = numero1 + numero2
# print("El resultado de la suma es:", resultado)

# CLASE 9 SOLUCION EJERCICIO CALIFICAR TU DIA
# Califica tu dia del 1 al 10
# resultado = int(input('Cómo estuvo tu día (1 al 10)?: '))
# print('Mi día estuvo de:', resultado)

# CLASE 10 OPERADORES ARITMETICOS
# operandoA = 3
# operandoB = 2
# suma = operandoA + operandoB
# print('Resultado suma:', suma)
# print(f'Resultado suma: {suma} ')

# CLASE 11 OPERADORES ARITMETICOS
# operandoA = 3
# operandoB = 2
# suma = operandoA + operandoB
# #print('Resultado suma:', suma)
# print(f'Resultado suma: {suma} ')
# resta = operandoA - operandoB
# print(f'Resultado resta: {resta} ')
# multiplicacion = operandoA * operandoB
# print(f'Resultado multiplicación: {multiplicacion}')
# division = operandoA / operandoB
# print(f'Resultado división: {division}')
# division = operandoA // operandoB # Esto es que nos devuelva el valor entero de la division
# print(f'Resultado división (int): {division}')
# modulo = operandoA % operandoB
# print(f'Resultado residuo división (módulo): {modulo}')
# exponente = operandoA ** operandoB
# print(f'Resultado exponente: {exponente}')

# CLASE 12 OPERADORES DE ASIGNACION
# miVariable = 10
# print(miVariable)
# miVariable = miVariable + 1
# print(miVariable)
# # incremento con reasignación
# miVariable += 1
# print(miVariable)
# # miVariable = miVariable - 2
# miVariable -= 2
# print(miVariable)
# # miVariable = miVariable * 3
# miVariable *= 3
# print(miVariable)
# miVariable /= 2
# print(miVariable)

# CLASE 13 OPERADORES COMPARACION
# a = 4
# b = 6

# resultado = a == b
# print(f'Resultado == : {resultado}')

# resultado = a != b
# print(f'Resultado != : {resultado}')

# resultado = a > b
# print(f'Resultado > : {resultado}')

# resultado = a >= b
# print(f'Resultado >= : {resultado}')

# resultado = a < b
# print(f'Resultado < : {resultado}')

# resultado = a <= b
# print(f'Resultado: <= {resultado}')


# CLASE 14 ALGORITMO DE NUMERO PAR
# a = int(input('Escribe un valor numérico: '))

# #print(a % 2)
# if a % 2 == 0:
#     print(f'El valor de a {a} es número par')
# else:
#     print(f'El valor de a {a} es número impar')


# #CLASE 15 ALGORITMO MAYOR DE EDAD
# edadAdulto = 18
# edadPersona = int(input("Proporciona tu edad: "))

# if edadPersona >= edadAdulto:
#     print(f'La persona con edad {edadPersona} es un adulto')
# else:
#     print(f'La persona con edad {edadPersona} es menor de edad')


# CLASE 16 OPERADORES LOGICOS
# a = True
# b = False
# resultado = a and b
# # print(resultado)

# resultado = a or b
# # print(resultado)

# resultado = not a
# print(resultado)


# CLASE 17 EJERCICIO DENTRO DE RANGO
# valor = int(input('Escribe el valor: '))
# valorMinimo = 0
# valorMaximo = 5

# dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)
# dentroRango = valor >= valorMinimo and valor <= valorMaximo

# if dentroRango:
#     print(f'El valor {valor} está dentro de rango')
# else:
#     print(f'El valor {valor} está fuera de rango')


# CLASE 18 EJERCICIO OPERADOR OR
# vacaciones = False
# diaDescanso = True

# if vacaciones or diaDescanso:
#     print('Puede asistir al juego')
# else:
#     print('Tiene deberes por hacer')


# CLASE 19 EJERCICIO OPERADOR NOT
# vacaciones = False
# diaDescanso = False

# if not (vacaciones or diaDescanso):
#     print('Tiene deberes por hacer')
# else:
#     print('Puede asistir al juego')


# CLASE 20 EJERCICIO VEINTES TREINTAS
# edad = int(input('Introduce tu edad: '))

# #veintes = edad >= 20 and edad < 30
# #print(veintes)
# #treintas = edad >= 30 and edad <40
# #print(treintas)

# if (edad >= 20 and edad < 30) or (edad >= 30 and edad <40):
#     print('Dentro de rango (20\'s) o (30\'s)')
# #    if veintes:
# #        print('Dentro de los 20\'s')
# #    elif treintas:
# #        print('Dentro de los 30\'s')
# #    else:
# #        print('Fuera de rango')
# else:
#     print("No está dentro de los 20's ni 30's")


# CLASE 21 SOLUCION TIENDA LIBROS
# print('Proporcione los siguientes datos del libro: ')
# nombre = input('Proporciona el nombre del libro: ')
# id = int(input('Proporciona el ID del libro: '))
# precio = float(input('Proporciona el valor de libro: '))
# envioGratuito = input('Indica si es envío gratuito (True/False): ')

# if envioGratuito == 'True':
#     envioGratuito = True
# elif envioGratuito == 'False':
#     envioGratuito = False
# else:
#     envioGratuito = 'Valor incorrecto, debe escribir True/False'

# print(f'''
#     Nombre: {nombre}
#     Id: {id}
#     Precio: {precio}
#     Envío Gratuito?: {envioGratuito}
# ''')


# CLASE 22 SENTENCIA IF ELSE
# condicion = False

# if condicion == True:
#     print('Condición verdadera')
# elif condicion == False:
#     print('Condición falsa')
# else:
#     print('Condición no reconocida')

# CLASE 23 EJERCICIO CONVERSION NUMERO TEXTO
# numero = int(input('Proporciona un valor entre 1 y 3: '))
# numeroTexto = ''
# if numero == 1:
#     numeroTexto = 'Número uno'
# elif numero == 2:
#     numeroTexto = 'Número dos'
# elif numero == 3:
#     numeroTexto = 'Número tres'
# else:
#     numeroTexto = 'Valor fuera de rango'
# print(f'Número proporcionado: {numero} - {numeroTexto}')


# CLASE 24 SINTAXIS SIMPLIFICADA ELSE IF
# condicion = False

# # if condicion:
# #     print('Condición verdadera')
# # else:
# #     print('Condición falsa')

# print('Condición verdadera') if condicion else print('Condición falsa')


# CLASE 25 EJERCICIO MES ESTACION
# mes = int(input('Proporciona mes del año (1-12): '))
# estacion = None
# if mes == 1 or mes == 2 or mes == 12:
#     estacion = 'Invierno'
# elif mes == 3 or mes == 4 or mes == 5:
#     estacion = 'Primavera'
# elif mes == 6 or mes == 7 or mes == 8:
#     estacion = 'Verano'
# elif mes == 9 or mes == 10 or mes == 11:
#     estacion = 'Otoño'
# else:
#     estacion = 'Mes incorrecto'
# print(f'Para el mes {mes} la estación es: {estacion}')


# CLASE 26 EJERCICIOS ETAPAS DE LA VIDA
# edad = int(input('Proporciona tu edad: '))
# mensaje = None
# if 0 <= edad < 10:
#     mensaje = 'La infancia es increíble...'
# elif  10 <= edad < 20:
#     mensaje = 'Muchos cambios, mucho estudio...'
# elif  20 <= edad < 30:
#     mensaje = 'Amor y comienza el trabajo...'
# else:
#     mensaje = 'Etapa de vida NO reconocida'
# print(f'Tu edad es: {edad}, {mensaje}')


# CLASE 27 CICLO WHILE
# # condicion = True
# #
# # while condicion:
# #     print('Ejecutando ciclo while')
# # else:
# #     print('Fin del ciclo while')

# contador = 0
# while contador < 3:
#     print(contador)
#     contador += 1 #contador = contador + 1
# else:
#     print('Fin ciclo while')


# CLASE 28 CICLO FOR
# cadena = 'Hola'

# for letra in cadena:
#     print(letra)
# else:
#     print('Fin ciclo for')


# CLASE 29 PALABRA BREAK (ROMPER CODIGO)
# for letra in 'Holanda':
#     if letra == 'a':
#         print(f'Letra encontrada: {letra}')
#         break
# else:
#     print('Fin ciclo for')


# CLASE 30 PALABRA CONTINUE
# # for i in range(6):
# #     if i % 2 == 0:
# #         print(f'Valor: {i}')

# for i in range(6):
#     if i % 2 != 0:
#         continue
#     print(f'Valor: {i}')


# CLASE 31 LISTAS EN PYTHON
# # Definir una lista de tipo str
# nombres = ['Juan','Karla','Ricardo', 'María']
# # imprimir la lista nombres
# print(nombres)
# # acceder a los elementos de un a lista
# print(nombres[0])
# print(nombres[1])
# # acceder a los elementos de manera inversa
# print(nombres[-1])
# print(nombres[-2])


# CLASE 32 LISTAS EN PYTHON PARTE 2
# # Definir una lista de tipo str
# nombres = ['Juan','Karla','Ricardo', 'María']
# # imprimir la lista nombres
# print(nombres)
# # acceder a los elementos de un a lista
# print(nombres[0])
# print(nombres[1])
# # acceder a los elementos de manera inversa
# print(nombres[-1])
# print(nombres[-2])
# #Imprimir un rago
# print(nombres[0:2]) # sin incluir el índice 2
# #Ir del inicio de la lista al índice (sin incluirlo)
# print(nombres[:3])
# #Desde el índice indicado hasta el final
# print(nombres[1:])
# #Cambiar un valor
# nombres[3] = 'Ivone'
# print(nombres)
# #iterar una lista
# for nombre in nombres:
#     print(nombre)
# else:
#     print('No existen más nombres en la lista')


# CLASE 33 LISTAS EN PYTHON PARTE 3
# # Definir una lista de tipo str
# nombres = ['Juan','Karla','Ricardo', 'María']
# # imprimir la lista nombres
# print(nombres)
# # acceder a los elementos de un a lista
# print(nombres[0])
# print(nombres[1])
# # acceder a los elementos de manera inversa
# print(nombres[-1])
# print(nombres[-2])
# #Imprimir un rago
# print(nombres[0:2]) # sin incluir el índice 2
# #Ir del inicio de la lista al índice (sin incluirlo)
# print(nombres[:3])
# #Desde el índice indicado hasta el final
# print(nombres[1:])
# #Cambiar un valor
# nombres[3] = 'Ivone'
# print(nombres)
# #iterar una lista
# for nombre in nombres:
#     print(nombre)
# else:
#     print('No existen más nombres en la lista')
# # preguntar el largo de una lista
# print(len(nombres))
# # agregar un elemento
# nombres.append('Lorenzo')
# print(nombres)
# # insertar un elemento en un índice en específico
# nombres.insert(1, 'Octavio')
# print(nombres)
# # remover un elemento
# nombres.remove('Octavio')
# print(nombres)
# # remover el último valor agregado
# nombres.pop()
# print(nombres)
# # eliminar un indice
# del nombres[0]
# print(nombres)
# # limpiar la lista
# nombres.clear()
# print(nombres)
# # borrar la lista por completo
# del nombres
# print(nombres)


# CLASE 34 TUPLAS PARTE 1
# #Definir una tupla
# frutas = ('Naranja', 'Plátano', 'Guayaba')
# print(frutas)
# #saber el largo
# print(len(frutas))
# #acceder a un elemento
# print(frutas[0])
# # navegación inversa
# print(frutas[-1])
# # acceder a un rango
# print(frutas[0:1])# sin incluir el último índice


# CLASE 35 TUPLAS PARTE 2
# #Definir una tupla
# frutas = ('Naranja', 'Plátano', 'Guayaba')
# print(frutas)
# #saber el largo
# print(len(frutas))
# #acceder a un elemento
# print(frutas[0])
# # navegación inversa
# print(frutas[-1])
# # acceder a un rango
# print(frutas[0:1])# sin incluir el último índice
# #recorrer elementos
# for fruta in frutas:
#     print(fruta, end=' ') # end se utiliza para reemplazar el valor de salto de linea por lo que le indiquemos
# #cambiar valor tupla
# # frutas[0] = 'Pera'
# frutasLista = list(frutas)
# frutasLista[0] = 'Pera'
# frutas = tuple(frutasLista)
# print('\n',frutas)
# #eliminar la tupla
# del frutas
# print(frutas)

# CLASE 36 SET
# # set
# planetas = {'Marte', 'Júpiter', 'Venus'}
# print(planetas)
# #largo
# print(len(planetas))
# # revisar si un elemento está presente
# print('Marte' in planetas)
# # agregar un elemento
# planetas.add('Tierra')
# print( planetas)
# #no se pueden duplicar elementos
# planetas.add('Tierra')
# print(planetas)
# # eliminar elemento posiblemente arrojando un error
# planetas.remove('Tierra')
# print(planetas)
# # eliminar elemento sin arrojar error
# planetas.discard('Júpiters')
# print(planetas)
# # limpiar set
# planetas.clear()
# print(planetas)
# # eliminar el set
# del planetas
# print(planetas)


# CLASE 37 DICCIONARIOS PARTE 1
# # dict (key, value)
# diccionario = {
#     'IDE':'Integrated Development Environment',
#     'OOP':'Object Oriented Programming',
#     'DBMS':'Database Management System'
# }
# print(diccionario)
# #largo
# print(len(diccionario))
# # acceder a un elemento (key)
# print( diccionario['IDE'])
# # otra forma de recuperar un elemento
# print(diccionario.get('OOP'))
# # modificando elementos
# diccionario['IDE'] = 'integrated development environment'
# print(diccionario)


# CLASE 38 DICCIONARIOS PARTE 2
# # dict (key, value)
# diccionario = {
#     'IDE':'Integrated Development Environment',
#     'OOP':'Object Oriented Programming',
#     'DBMS':'Database Management System'
# }
# print(diccionario)
# #largo
# print(len(diccionario))
# # acceder a un elemento (key)
# print( diccionario['IDE'])
# # otra forma de recuperar un elemento
# print(diccionario.get('OOP'))
# # modificando elementos
# diccionario['IDE'] = 'integrated development environment'
# print(diccionario)
# # recorrer los elementos
# for termino, valor in diccionario.items():
#     print(termino, valor)
#
# for termino in diccionario.keys():
#     print(termino)
#
# for valor in diccionario.values():
#     print(valor)
#
# # comprobar existencia de algún elemento
# print('IDE' in diccionario)
#
# # agregar un elemento
# diccionario['PK'] = 'Primary Key'
# print(diccionario)
#
# # remover un elemento
# diccionario.pop('DBMS')
# print(diccionario)
#
# # limpiar
# diccionario.clear()
# print(diccionario)
#
# # eliminar el diccionario
# del diccionario
# print(diccionario)


# CLASE 39 FUNCIONES
# def mi_funcion():
#     print('saludos desde mi función')

# mi_funcion()


# CLASE 40 FUNCIONES CON PASO DE ARGUMENTOS
# def mi_funcion(nombre, apellido):
#     print('saludos desde mi función')
#     print(f'Nombre: {nombre}, Apellido: {apellido}')

# mi_funcion('Juan', 'Perez')
# mi_funcion('Karla','Lara')


# CLASE 41 FUNCIONES CON RETURN
# def sumar(a, b):
#     return a + b

# resultado = sumar(5, 3)
# print(f'Resultado sumar: {resultado}')
# # print(f'Resultado sumar: {sumar(5,3}')


# CLASE 42 VALORES DEFAULTO EN PARAMETROS FUNCIONES
# def sumar(a:int = 0, b: int = 0):
#     return a + b

# resultado = sumar()
# print(f'Resutlado sumar: {resultado}')

# print(f"Resultado sumar: {sumar(2,8)}")

# CLASE 43 ARGUMENTOS VARIABLES
# def listarNombres(*nombres):
#     for nombre in nombres:
#         print(nombre)
#
# listarNombres('Juan', 'Karla', 'María', 'Ernesto')
# listarNombres('Laura', 'Carlos')


# CLASE 44 DICCIONARIOS VARIABLE
# def listarTerminos(**terminos):
#     for llave, valor in terminos.items():
#         print(f'{llave}: {valor}')

# listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
# listarTerminos(DBMS='Database Management System')

# CLASE 45 DISTINTOS TIPOS DE DATOS EN FUNCION
# def desplegarNombres(nombres):
#     for nombre in nombres:
#         print(nombre)

# nombres = ['Juan', 'Karla', 'Guillermo']
# desplegarNombres(nombres)
# desplegarNombres('Carlos')
# desplegarNombres((8, 9))
# desplegarNombres([10, 11])


# CLASE 46 FUNCIONES RECURSIVAS
# # 5! = 5 * 4 * 3 * 2 * 1
# # 5! = 5 * 4 * 3 * 2
# # 5! = 5 * 4 * 6
# # 5! = 5 * 24
# # 5! = 120
# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero * factorial(numero-1)

# numero = 5
# resultado = factorial(numero)
# print(f'El factorial de {numero} es {resultado}')

# TAREA
# # Función que calcula el impuesto de un pago
# def calcular_total(pago_sin_impuesto, impuesto):
#     return pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
#
# # Ejecutamos la función
# pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
# impuesto = float(input('Proporcione el monto del impuesto: '))
# pago_con_impuesto = calcular_total(pago_sin_impuesto, impuesto)
# print(f'Pago con impuesto: {pago_con_impuesto}')

# TAREA
# import os
#
#
# def celsius_fahrenheit(celsius):
#     return celsius * 9/5 + 32
#
# def fahrenheit_celsius(fahrenheit):
#     return (fahrenheit -32) * 5/9
#
# def menu():
#     print("1. Convertir de grados fahrenheit a grados celsius")
#     print("2. Convertir de grados celsius a grados fharenheit")
#     print("3. Salir")
# opc = 0
# while(opc != 3):
#     menu()
#     opc = int(input("Por favor ingrese una opcion: "))
#     if(opc == 1):
#         fahrenheit = float(input("Ingrese los grados fahrenheit: "))
#         print(fahrenheit_celsius(fahrenheit))
#     elif(opc == 2):
#         celsius  = float(input("Ingrese los grados celsius: "))
#         print(celsius_fahrenheit(celsius))
#     elif(opc == 3):
#         print("Gracias por utilizar nuestro programa :D")
#         os.system("cls")
#     else:
#         print("No ingreso una opcion valida")


# CLASE 47 CLASES Y OBJETOS
# El ejercicio se encuentra en el archivo Persona.py


# CLASE 48 CLASES Y OBJETOS PARTE 2
# Esta en el archivo Persona.py


# CLASE 49 CLASES Y OBJETOS CON PASO DE ARGUMENTOS
# Esta en el archivo de Persona.py


# CLASE 50 CREACION DE MAS OBJETOS DE UNA CLASE
# Esta en el archivo de Persona.py


# CLASE 51 REFERENCIA DE MEMORIA DE OBJETOS  Y EJECUCICIO PASO A PASO
# Esta en el archivo de Persona.py


# CLASE 52 MODIFICAR ATRIBUTOS DE UN OBJETO
# Esta en el archivo de Persona.py


# CLASE 53 METODOS DE INTANCIA EN PYTHON
# Esta en el archivo de Persona.py


# CLASE 54 MAS DE self Y ATRIBUTOS DE INSTANCIA EN PYTHON
# ESta en el archivo de Persona.py


# CLASE 55 EJERCICIO CLASE ARITMETICA
# ESta en el archivo de Aritmetica.py


# CLASE 56 EJERCICIO CLASE ARITMETICA
# ESta en el archivo de Aritmetica.py


# TAREA LABORATORIO RECTANGULO
# Se encuentra en el archivo Aritmetica.py


# TAREA LABORATORIO CUBO
# Se encuentra en el archivo Aritmetica.py


# CLASE 57 ROBUSTECIENDO EL METODO INIT
# Se encuentra en el archivo Persona.py


# CLASE 58 ENCAPSULAMIENTO EN PYTHON
# Se enceuntra en el archivo Persona.py


# CLASE 59 METODOS GET Y SET EN PYTHON
# Se enceuntra en el archivo Persona.py


# CLASE 60 ATRIBUTOS READ-ONLY(SOLO LECTURA) EN PYTHON
# Se encuentra en el archivo Persona.py


# CLASE 61 ENCAPSULANDO TODOS LOS ATRIBUTOS DE UNA CLASE
# SE encuentra en el archivo Persona.py


# CLASE 62 USO DE MODULOS Y CLASES EN PYTHON
# Se encuentra en el archivo Persona.py el esqueleto y en la PruebaPersona.py


# CLASE 63 COMPROBACION DEL MODULO PRINCIPAL EN PYTHON
# Se encuentra en el archivo Persona.py el esqueleto y en la PruebaPersona.py


# CLASE 64 DESTRUCTOR DE OBJETOS EN PYTHON
# Se encuentra en el archivo Persona.py el esqueleto y en la PruebaPersona.py


# CLASE 65 EJEMPLO DE HERENCIA EN PYTHON
# Se encuentra en el archivo Persona.py


# CLASE 66 SOBREESCRITURA DEL METODO __str__() EN PYTHON
# Se encuentra en el archivo Persona.py el esqueleto y en el ClientePersona.py


# TAREA: EJERCICIO HERENCIA EN PYTHON
# Se encuentra en el archivo Persona.py


# CLASE 67 HERENCIA MULTIPLE EN PYTHON
# Se encuentra en el archivo FiguraGeometrica.py y Color.py


# CLASE 68 HERENCIA MULTIPLE EN PYTHON PARTE 2
# Se encuentra en el archivo FiguraGeometrica.py, Color.py y Cuadrado.py


# CLASE 69 HERENCIA MULTIPLE EN PYTHON PARTE 3
# Se encuentra en el archivo FiguraGeometrica.py, Color.py, Cuadrado.py y test_figura_geometrica.py


# CLASE 70 METODO MRO - METHOD RESOLUTION ORDER EN PYTHON
# Se encuentra en el archivo FiguraGeometrica.py, Color.py, Cuadrado.py y test_figura_geometrica.py


# LABORATORIO: FIGURA GEOMETRICA
# Se encuentra en el archivo FiguraGeometrica.py, Color.py, Cuadrado.py y test_figura_geometrica.py


# LABORATORIO: FIGURA GEOMETRICA SOLUCION UBALDO
# Se encuentra en el archivo FiguraGeometrica.py, Color.py, Cuadrado.py y test_figura_geometrica.py


# CLASE 71 CLASES ABSTRACTAS EN PYTHON
# Se encuentra en el archivo FiguraGeometrica.py, Color.py, Cuadrado.py y test_figura_geometrica.py
# No se pueden crear objetos de una clase abstracta y todos los metodos que se encuentre alli se deberan de sobreescribir


# CLASE 72 VARIABLES DE CLASE EN PYTHON
# Se encuentra en el archivo MIclase.py


# CLASE 73 CREACION DE VARIABLES DE CLASE AL VUELO EN PYTHON
# Se encuentra en el archivo Miclase.py


# CLASE 74 METODOS ESTATICOS EN PYTHON
# Se encuentra en el archivo Miclase.py


# CLASE 75 METODOS DE CLASE EN PYTHON
# Se encuentra en el archivo Miclase.py


# CLASE 76 CONTEXTO ESTATICO Y DINAMICO EN PYTHON
# Se encuentra en el archivo Miclase.py


# CLASE 76 CONSTANTES EN PYTHON
# Se encuentra en el archivo Constantes.py


# CLASE 77 EJERCICIO CONTADOR OBJETOS
# Se encuentra en el archivo Persona.py


# CLASE 78 POSIBLE MEJORA EJERCICIO CONTADOR PERSONA
# Se encuentra en el archivo Persona.py


# Clase 79 DISEÑO DE CLASES EN PYTHON
# Mostrando el diagrama UML se encuentra en disenio_clases.png

# CLASE 80 CREACION CLASE PRODUCTO
# Se encuentra en el archivo Producto.py


# CLASE 81 CREACION CLASE ORDEN
# Se encuentra en el archivo Producto.py y Orden.py


# CLASE 82 PRUEBA DE LAS CLASES ORDENES Y PRODUCTOS
# Se encuentra en el archivo Producto.py y Orden.py


# CLASE 83 SOBRECARGA DE OPERADORES EN PYTHON
# Se encuentra en el archivo de sobrecargar_operadores.py


# CLASE 84 SOBRECARGA DE OPERADORES EN PYTHON - PARTE 2
# Se encuentra en el archivo de sobrecargar_operadores.py y Persona.py


# CLASE 85 POLIMOFRISMO EN PYTHON - PARTE 1
# Se encuentra en el archivo Gerente.py y Empleado.py


# CLASE 86 POLIMOFRISMO EN PYTHON - PARTE 2
# Se encuentra en el archivo Gerente.py, Empleado.py y test_polimorfismo


# CLASE 87 METODO ISINSTANCE Y POLIMORFISMO EN PYTHON AND METODO DEBUG
# Se encuentra en el archivo Gerente.py, Empleado.py y test_polimorfismo
# from TareaMundoPc.DispositivoEntrada import Persona


# TAREA LABORATORIO MUNDO PC
# Se encuentra mi solucion en la caprta TareaMundoPc y la solucion de Ubaldo en el paquete mundo_pcUbaldo


# CLASE 88 MANEJO DE ERRORES O EXCEPCIONES EN PYTHON
# Se encuentra en el paquete ManejoExceptionesPython (manejo_excepciones.py)


# CLASE 89 PROCESAMIENTO DE EXCEPCIONES EN PYTHON
# Se encutnra en el paquete ManejoExceptionesPython (manejo_excepciones.py)


# CLASE 90 PROCESAR CLASES DE EXCEPCION MAS ESPECIFICAS
# Se encuentra en el paquete ManejoExceptionesPython (manejo_excepciones.py)


# CLASE 91 MAS DE PROCESAMIENTO DE EXCEPCIONES
# Se encuentra en el paquete ManejoExceptionesPython (manejo_excepciones.py)


# CLASE 92 BLOQUE ELSE Y FINALLY AL MANEJAR EXCEPCIONES
# Se encuentra en el paquete ManejoExceptionesPython (manejo_excepciones.py)


# CLASE 92 CREACION DE CLAESE DE EXCEPCION PERSONALIZADAS
# Se encuentra en el paquete ManejoExceptionesPython (manejo_excepciones.py)


# CLASE 93 MANEJO DE ARCHIVOS EN PYTHON
# Se encuentra en el paquete ManejoArchivosPython (manejo_archivos.py)


# CLASE 94 ESPECIFICAR EL JUEGO DE CARACTERES DE UN ARCHIVO DE TEXTO
# Se encuentra en el paquete ManejoArchivosPython (manejo_archivos.py)


# CLASE 95 LECTURA DE ARCHIVOS EN PYTHON
# Se encuentra en el paquete ManejoArchivosPython (leer_archivo.py)


# CLASE 96 MAS FORMAS DE TRABAJAR CON ARCHIVOS EN PYTHON
# Se encuentra en el paquete ManejoArchivosPython (leer_archivo.py)


# CLASE 97 USO DE WITH, ARCHIVOS Y CONTEXT MANAGER CON PYTHON
# Se encuentra en el paquete ManejoArchivosPython (Archivos_con_with.py)

# CLASE 98 USO DE WITH Y CONTEXT MANAGER CON PYTHON
# Se encuentra en el paquete ManejoArchivosPython (Archivos_con_with.py)

# SECCION 22 PROYECTO FINAL -CATALOGO DE PELÍCULAS
# Se encuentra en el paquete de catalogoPeliculas


# CLASE 99 INSTALCION DEL MODULO DE POSTGRESQL EN PYTHON
# pip comando que nos permite actualizar instalar o eliminar paquetes en este caso vamos a instalar(pip install psycopg2)
# Que es la libreria que vamos a utilizar para conectar a python con postgreSQL


# CLASE 100 (FELICITACIONES) CONEXION DE P YTHON A POSTGRESQL
# Se encuentra en el paquete UsoPostgresSQL