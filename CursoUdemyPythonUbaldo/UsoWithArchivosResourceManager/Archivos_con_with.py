# CLASE 97 USO DE WITH, ARCHIVOS Y CONTEXT MANAGER CON PYTHON
# De manera automatica abre y cierra el archivo contexto manager o administrador de recursos
# with open('C:\\Users\\USUARIO\\Documents\\CursosUdemi\\CursoUdemyPythonUbaldo\\ManejoArchivosPython\\prueba.txt',
#           'r', encoding='utf8') as archivo:
#     print(archivo.read())
#
#     #__enter__ # metodo que abre el archivo
#     #__exit__ # donde se cierra el archivo
#


# CLASE 98 USO DE WITH Y CONTEXT MANAGER CON PYTHON
# with open('C:\\Users\\USUARIO\\Documents\\CursosUdemi\\CursoUdemyPythonUbaldo\\ManejoArchivosPython\\prueba.txt',
#           'r', encoding='utf8') as archivo:
#     print(archivo.read())
#
#     #__enter__ # metodo que abre el archivo
#     #__exit__ # donde se cierra el archivo
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('C:\\Users\\USUARIO\\Documents\\CursosUdemi\\CursoUdemyPythonUbaldo\\ManejoArchivosPython\\prueba.txt') as archivo:
    print(archivo.read())