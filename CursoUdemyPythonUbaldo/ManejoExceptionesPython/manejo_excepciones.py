# CLASE 88 MANEJO DE ERRORES O EXCEPCIONES EN PYTHON
# try:
#     10/0
# except Exception as e: # Clase que maneja todos las excepciones Exception
#     print(f'Ocurrio un error: {e}')

# CLASE 89 PROCESAMIENTO DE EXCEPCIONES EN PYTHON
# resultado = None
# a = 10
# b = 0
# try:
#     resultado = a / b  # No se va ejecutar porque arroja un error, asi que se ejecuta el codigo de except
# except ZeroDivisionError as e:
#     print(f'Ocurrio un error: {e}')
#
# print(f'Resultado: {resultado}')
# print('Coninuamos...')
#
# resultado = None
# a = '10'
# b = 0
# try:
#     resultado = a / b
# except Exception as e:
#     print(f'Ocurrio un error: {e}')
#
# try:
#     resultado = a / b
#
# except:
#     print("Error")

# CLASE 90 PROCESAR CLASES DE EXCEPCION MAS ESPECIFICAS
# resultado = None
# a = '10'
# b = 0
# try:
#     resultado = a / b
# except ZeroDivisionError as zde:
#     print(f'Ocurrio un error: {zde}, {type(zde)}')
# except TypeError as e:
#     print(f"Ocurrio un error: {e}, {type(e)}")
# except Exception as e:
#     print(f'Ocurrio un error: {e}, {type(e)}')
#
# print(f'Resultado: {resultado}')
# print('Continuamos')


# CLASE 91 MAS DE PROCESAMIENTO DE EXCEPCIONES
# resultado = None # Se debe aclarar que esta variable es global
# try:
#     # Si declaramos una variable dentro del bloque de try: except: esto solo podra ser utilizada dentro de estemismo bloque
#     a = int(input('Primer número: '))
#     b = int(input('Segundo número: '))
#     resultado = a / b
# except ZeroDivisionError as zde:
#     print(f'Ocurrio un error: {zde}, {type(zde)}')
# except TypeError as e:
#     print(f"Ocurrio un error: {e}, {type(e)}")
# except ValueError as e:
#     print(type(e), f"Error {e}")
# except Exception as e:
#     print(f'Ocurrio un error: {e}, {type(e)}')
#
# print(f'Resultado: {resultado}')
# print('Continuamos')


# CLASE 92 BLOQUE ELSE Y FINALLY AL MANEJAR EXCEPCIONES
resultado = None
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    resultado = a / b
except ZeroDivisionError as zde:
    print(f'Ocurrio un error: {zde}, {type(zde)}')
except TypeError as e:
    print(f"Ocurrio un error: {e}, {type(e)}")
except ValueError as e:
    print(type(e), f"Error {e}")
except Exception as e:
    print(f'Ocurrio un error: {e}, {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos')
