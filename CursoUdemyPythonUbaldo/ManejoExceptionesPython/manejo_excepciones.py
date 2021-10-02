# CLASE 87 MANEJO DE ERRORES O EXCEPCIONES EN PYTHON
# try:
#     10/0
# except Exception as e: # Clase que maneja todos las excepciones Exception
#     print(f'Ocurrio un error: {e}')

# CLASE 88 PROCESAMIENTO DE EXCEPCIONES EN PYTHON
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

# CLASE 89 PROCESAR CLASES DE EXCEPCION MAS ESPECIFICAS
resultado = None
a = '10'
b = 0
try:
    resultado = a / b
except ZeroDivisionError as zde:
    print(f'Ocurrio un error: {zde}, {type(zde)}')
except TypeError as e:
    print(f"Ocurrio un error: {e}, {type(e)}")
except Exception as e:
    print(f'Ocurrio un error: {e}, {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos')