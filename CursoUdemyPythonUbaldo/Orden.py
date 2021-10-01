# CLASE 80 CREACION CLASE ORDEN
# from Producto import Producto as P
#
#
# class Orden:
#     contador_ordenes = 0
#
#     def __init__(self, productos):
#         Orden.contador_ordenes += 1
#         self.__id_orden = Orden.contador_ordenes
#         self.__productos = list(productos)
#
#     @property
#     def id_orden(self):
#         return self.__id_orden
#
#     @id_orden.setter
#     def id_orden(self, id_orden):
#         self.id_orden = id_orden
#
#     @property
#     def productos(self):
#         return self.__productos
#
#     @productos.setter
#     def productos(self, productos):
#         self.__productos = list(productos)
#
#     def agregar_producto(self, producto):
#         self.__productos.append(producto)
#
#     def caclular_total(self):
#         total = 0
#         for producto in self._productos:
#             total += producto.precio
#         return total
#
#     def __str__(self):
#         productos_str = ''
#         for producto in self.productos:
#             productos_str += producto.__str__() + '|'
#         return f'Orden: {self.id_orden}, \nProductos: {productos_str}'
#
#
# if __name__ == '__main__':
#     producto1 = P('Camisa', 100.00)
#     print(producto1)
#     producto2 = P('Pantalon', 150.00)
#     print(producto2)
#     productos1 = [producto1, producto2]
#     orden1 = Orden(productos1)
#     print(orden1)
#     orden2 = Orden(productos1)
#     print(orden2)


# CLASE 81 PRUEBA DE LAS CLASES ORDENES Y PRODUCTOS
# from Producto import Producto as P
#
#
# class Orden:
#     contador_ordenes = 0
#
#     def __init__(self, productos):
#         Orden.contador_ordenes += 1
#         self.__id_orden = Orden.contador_ordenes
#         self.__productos = list(productos)
#
#     @property
#     def id_orden(self):
#         return self.__id_orden
#
#     @id_orden.setter
#     def id_orden(self, id_orden):
#         self.id_orden = id_orden
#
#     @property
#     def productos(self):
#         return self.__productos
#
#     @productos.setter
#     def productos(self, productos):
#         self.__productos = list(productos)
#
#     def agregar_producto(self, producto):
#         self.__productos.append(producto)
#
#     def calcular_total(self):
#         total = 0
#         for producto in self.productos:
#             total += producto.precio
#         return total
#
#     def __str__(self):
#         productos_str = ''
#         for producto in self.productos:
#             productos_str += producto.__str__() + '|'
#         return f'Orden: {self.id_orden}, \nProductos: {productos_str}'
#
#
# if __name__ == '__main__':
#     producto1 = P('Camisa', 100.00)
#     print(producto1)
#     producto2 = P('Pantalon', 150.00)
#     print(producto2)
#     productos1 = [producto1, producto2]
#     orden1 = Orden(productos1)
#     print(orden1)
#     orden2 = Orden(productos1)
#     print(orden2)