# CLASE 95 LECTURA DE ARCHIVOS EN PYTHON
# try:
#     # En el caso de que queramos abrir un archivo que se encuentra en otra carpeta se debera de especificar la ruta de windows, mac o linux
#     archivo = open('prueba.txt', 'r', encoding = 'utf8')
#     # print(archivo.read()) # Despues de que leamos el archivo ya se habra
#     # terminado de leer el archivo, asi que no podremos volver a leerlo
#     # Leer algunos caracteres
#     # archivo.read(cantidad de caracteres que queremos leer)
#     # estos se acumularan asi que queremos volver a ejecutarlo
#     # ya habriamos leido la cantidad que indicamos y leera
#     # despues la otra cantidad si es que hay mas
#     # print(archivo.read(5))
#     # print(archivo.read(3))
#
#     # Leer lineas completas
#     print(archivo.readline())
#     print(archivo.readline())
# except BaseException as e:
#     print(e)
#

# CLASE 96 MAS FORMAS DE TRABAJAR CON ARCHIVOS EN PYTHON
archivo = open('C:\\Users\\USUARIO\\Documents\\CursosUdemi\\CursoUdemyPythonUbaldo\\ManejoArchivosPython\\prueba.txt'
               , 'r', encoding='utf8')
# Nosotros podemos agregar información directamente al archivo y imprimirla aqui
# for linea in archivo: # Podemos recorrer las lineas del archivo con un for
#     print(linea)

# Esto nos devolvera una lista con las lineas que tenemos en el archivo
# print(archivo.readlines())

# Acceder a una linea de la lista pero solo a una de ellas si intentamos utilizar este metodo de nuevo saldra un error
# print(archivo.readlines()[1])

# Podemos copiar el archivo original vaciandolo en uno nuevo
# a - anexar informacion debemos de tener cuidado puesto que estaremos copiando el mismo texto varias veces
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo2.close()
archivo2.close()
archivo2 = open('copia.txt', 'r', encoding='utf8')
print(archivo2.read())
del archivo2