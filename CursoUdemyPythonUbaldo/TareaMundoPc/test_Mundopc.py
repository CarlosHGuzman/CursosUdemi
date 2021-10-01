from Orden import Orden
from Computadora import Computadora

computadora = Computadora('usb', 'usb', 'Hp', 'Hp', 'Hp', '15 pulgadas')
orden1 = Orden()
orden1.agregarComputadora(computadora)
print(orden1)