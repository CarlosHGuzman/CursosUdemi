# CLASE 93 MANEJO DE ARCHIVOS EN PYTHON
# try:
#     #El metodo open indica que podemos abrir un archivo ya existente
#     # o podemos crear ese archivo, la w en este caso indica que vamos a escribir
#     # variable = open('nombre.extension', 'tipo', codigo de caracteres)
#     archivo = open('prueba.txt', 'w')
#     archivo.write('Agregamos informacion al archivo\n')
#     archivo.write('Adios')
# except Exception as e:
#     print(e)
# finally:
#     # variable.close() va a indicar que vamos a cerrar el archivo
#     archivo.close()


# CLASE 94 ESPECIFICAR EL JUEGO DE CARACTERES DE UN ARCHIVO DE TEXTO
# try:
#     # El metodo open indica que podemos abrir un archivo ya existente
#     # o podemos crear ese archivo, la w en este caso indica que vamos a escribir
#     # variable = open('nombre.extension', 'tipo', codigo de caracteres)
#     archivo = open('prueba.txt', 'w', encoding = 'utf8')
#     archivo.write('Agregamos información al archivo\n')
#     archivo.write('Adios')
# except Exception as e:
#     print(e)
# finally:
#     # variable.close() va a indicar que vamos a cerrar el archivo
#     archivo.close()
#     print('Se ha cerrado el archivo')
#     #archivo.write('nueva info') # Despues de que cerremos el archivo no se puede utilizar
#
# CLASE 95 LECTURA DE ARCHIVOS EN PYTHON
try:
    # El metodo open idncia que podemos abrir un archivo ya existente
    # o podemos crear ese archivo, la w en este caso indica que vamos a escribir
    # variable = open('nombre.extension', 'tipo', enconding)
    archivo = open('prueba.txt', 'r', encoding = 'utf8')
    archivo.write('Agregamos informacion al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print('hola xd',e)
finally:
    # variable.close() va a indicar que vamos a cerrar el archivo
    archivo.close()
    print('Se ha cerrado el archivo')
    # archivo.wirte('nueva info') # Despues de que cerremos el archiov no se puede utilizar

try:
    modoAbrirArchivo = open('modoAbrirArchivo.doc', 'w', encoding = 'utf8')
    modoAbrirArchivo.write('''
"r" - Read- Default value, Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist. Se va anexar la  informacion y no eliminara la que ya existe
"w" - Write - Opens a file for writin, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exist

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Defalult value. Text m ode
"b" - Binary - Binary mode (e.g. images)

Ademas podemos combinar algunos modos como lo son 

"w+" que va indicar que podemos escribir pero tambien para leer
"r+" que va indicar que podemos leer la información, pero tambien para escribir información
    ''')
except Exception as e:
    print(e)
finally:
    modoAbrirArchivo.close()
    print('Se cerro el archivo modo de abrir archivo')