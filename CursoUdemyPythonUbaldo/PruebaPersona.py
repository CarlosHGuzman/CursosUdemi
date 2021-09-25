# CLASE 62 USO DE MODULOS Y CLASES EN PYTHON
# from archivo import clase o para importar todas las clases colocamos *
# from Persona import Persona
#
# persona1 = Persona('CarLos', 'GuzmAn', 30)
# persona1.mostrar_detalles()


# CLASE 63 COMPROBACION DEL MODULO PRINCIPAL EN PYTHON
# from archivo import clase o para importar todas las clases colocamos *
# from Persona import Persona
#
# persona1 = Persona('CarLos', 'GuzmAn', 30)
# persona1.mostrar_detalles()


# CLASE 64 DESCTRUCTOR DE OBJETOS EN PYTHON
# from archivo import clase o para importar todas las clases colocamos *
from Persona import Persona

print('Creacion objetos'.center(30, '-'))
persona1 = Persona('CarLos', 'GuzmAn', 30)
persona1.mostrar_detalles()

print('Eliminacion de objetos'.center(30, '-'))
del persona1
