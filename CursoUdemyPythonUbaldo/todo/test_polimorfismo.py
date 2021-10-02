# CLASE 86 POLIMOFRISMO EN PYTHON - PARTE 2
# from Empleado import Empleado
# from Gerente import Gerente
#
# def imprimir_detalles(objeto):
#     # print(objeto)
#     print(type(objeto))
#     print(objeto.mostrar_detalles())
#
#
# empleado = Empleado('Carlos Guzman', 5000)
# imprimir_detalles(empleado)
#
# gerente = Gerente('Humberto Ramirez', 5000, 'Sistemas')
# imprimir_detalles(gerente)


# CLASE 87 METODO ISINSTANCE Y POLIMORFISMO EN PYTHON AND METODO DEBUG
from todo.Empleado import Empleado
from todo.Gerente import Gerente

def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Carlos Guzman', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Humberto Ramirez', 5000, 'Sistemas')
imprimir_detalles(gerente)