# CLASE 47 CLASES Y OBJETOS
# class Persona:
#     pass #Solo para que se cree y permita que este vacio
#
# print(type(Persona))


# CLASE 48 CLASES Y OBJETOS PARTE 2
# class Persona:
#     #mi_atributo = '' #Esta no es la forma de iniciar un atributo puesto que ya seria un atributo de la clase
#     def __init__(self): #El metodo __init__ es para crear un constructor
#         self.nombre = "Juan"#El cual inicializara los atributos de la clase
#         self.apepllido = 'Perez'
#         self.edad = 28  # self indica que es de este objeto
#
# #variable = Clase(parametros) no es necesario pasarle el parametro para self
# persona1 = Persona() # en esta parte se inicializa un objeto el cual llamara al metodo init que es nuestro constructor automaticamente
# print(persona1) # esto imprime la direccion en memoria
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad) # para acceder a un atributo o metodo es variable.metodo_atributo


# #CLASE 49 CLASES Y OBJETOS CON PASO DE ARGUMENTOS
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
# #Se deben pasar los argumentos que especificamos en el constructor __init__
# persona1 = Persona('Carlos' , "Guzman", 28)
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)


# CLASE 50 CLASES Y OBJETOS CON PASO DE ARGUMENTOS
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#
# # Se deben pasar los argumentos que especificamos en el constructor __init__
# persona1 = Persona('Carlos', "Guzman", 28)
# print(f"Objeto persona 1: {persona1.nombre} {persona1.apellido} ´{persona1.edad}")
#
# persona2 = Persona('Carlos', "Ramirez", 18)
# print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')


# CLASE 51 CLASES Y OBJETOS CON PASO DE ARGUMENTOS
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#
# # Se deben pasar los argumentos que especificamos en el constructor __init__
# persona1 = Persona('Carlos', "Guzman", 28) # PUNTO DE RUPTURA
# print(f"Objeto persona 1: {persona1.nombre} {persona1.apellido} ´{persona1.edad}")
#
# persona2 = Persona('Carlos', "Ramirez", 18)
# print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')


# CLASE 52 MOFICIAR LOS ATRIBUTOS DE UN OJBETO
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


# Se deben pasar los argumentos que especificamos en el constructor __init__
# persona1 = Persona('Carlos', "Guzman", 28) # PUNTO DE RUPTURA
# print(f"Objeto persona 1: {persona1.nombre} {persona1.apellido} ´{persona1.edad}")
#
# persona1.nombre = "cArlos"
# persona1.apellido = 'GuzMan'
# persona1.edad  = 19
# print(f"Objeto persona 1: {persona1.nombre} {persona1.apellido} ´{persona1.edad}")
#
#
# persona2 = Persona('Carlos', "Ramirez", 18)
# print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
#
# persona2.nombre = "carLOS"
# persona2.apellido = "guzMAN"
# persona2.edad = 23
# print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')


# CLASE 53 METODOS DE INTANCIA EN PYTHON
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#     def mostrar_Detalle(self):  # tiene que recibir si o si el parametro de self
#         print(f"Persona: {self.nombre} {self.apellido} {self.edad}")
#         # Para acceder a los atributos dentro de la clase siempre se les debara colocar self.atributo
#
#
# # Se deben pasar los argumentos que especificamos en el constructor __init__
# persona1 = Persona('Carlos', "Guzman", 28)  # PUNTO DE RUPTURA
# persona1.mostrar_Detalle()
# persona2 = Persona('Carlos', "Ramirez", 18)
# persona2.mostrar_Detalle()


# CLASE 54 MAS DE self Y ATRIBUTOS DE INSTANCIA EN PYTHON
# class Persona:
#     # No necesariamente el parametro self se tiene que llamar asi le puedes colocar caulquier nombre
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#     def mostrar_Detalle(self):  # tiene que recibir si o si el parametro de self
#         print(f"Persona: {self.nombre} {self.apellido} {self.edad}")
#         # Para acceder a los atributos dentro de la clase siempre se les debara colocar self.atributo
#
#
# # Se deben pasar los argumentos que especificamos en el constructor __init__
# persona1 = Persona('Carlos', "Guzman", 28)  # PUNTO DE RUPTURA
# # persona1.mostrar_Detalle()
# Persona.mostrar_Detalle(persona1)  # Tambien se puede llamar desde la clase pasandole el argumento del objeto
# # Si no se le pasa el argumento objeto no funcionara como deberia y arrojara un error
# persona1.telefono = "3127914365"  # Se puede crear un atributo desde fuera de la clase pero este sera local al objeto
# # Es decir que los otros objetos que creemos no tendran este atributo
# print(persona1.telefono)
#
# persona2 = Persona('Carlos', "Ra0mirez", 18)
# persona2.mostrar_Detalle()
# # print(persona2.telefono) # Error


# CLASE 57 ROBUSTECIENDO EL METODO INIT
# class Persona:
#     def __init__(self, nombre, apellido, edad, *valores, **terminos):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.valores = valores
#         self.terminos = terminos
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')
#
# persona1 = Persona("Carlos", "Guzman" , 18, '44553322', 2,3,4 ,5, m='manzana', p = 'pera')
# persona1.mostrar_detalle()
#
# persona2 = Persona("CARlos", "GUZman", 18) # No es necesario pasar los valores de la tupla o del diccionario
# persona2.mostrar_detalle()


# CLASE 58 ENCAPSULAMIENTO EN PYTHON
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         # Cuando se coloca _ significa que el atributo esta encapsulado
#         # Ejemplos _nombre esto si permitira la modificacion pero sera como una indicacion que no se debe de hacer
#         # __nombre no permitira hacer la modificacion fuera de la clase pero no es lo mas comun
#         self._nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#     def mostrar_detalles(self):
#         print(f'Persona: {self._nombre} {self.apelllido} {self.edad}')
#
#
# persona1 = Persona('Carlos', "Guzman", 18, '3127914365')
# persona1._nombre = 'CaRlos GuZman'
# persona1.mostrar_detalles()


# CLASE 59 ENCAPSULAMIENTO EN PYTHON
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         # Cuando se coloca _ significa que el atributo esta encapsulado
#         # Ejemplos _nombre esto si permitira la modificacion pero sera como una indicacion que no se debe de hacer
#         # __nombre no permitira hacer la modificacion fuera de la clase pero no es lo mas comun
#         self._nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#     # Decorador indica que vamos a cambiar el comportamiento de nuestro metodo
#     # En general permite no colocar los parentesis al final de la llamada
#     @property
#     def nombre(self):
#         print('Llamando metodo get nombre')
#         return self._nombre
#
#     @nombre.setter
#     def nombre(self, nombre):
#         print("Lamando metodo set nombre")
#         self._nombre = nombre
#
#     def mostrar_detalles(self):
#         print(f'Persona: {self._nombre} {self.apelllido} {self.edad}')
#
#
# persona1 = Persona('Carlos', "Guzman", 18)
# print(persona1.nombre)
# persona1.nombre = 'CArlos HUmberto'
# print(persona1.nombre)


# CLASE 60 ATRIBUTOS READ-ONLY(SOLO LECTURA) EN PYTHON
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         # Cuando se coloca _ significa que el atributo esta encapsulado
#         # Ejemplos _nombre esto si permitira la modificacion pero sera como una indicacion que no se debe de hacer
#         # __nombre no permitira hacer la modificacion fuera de la clase pero no es lo mas comun
#         self._nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#     # Decorador indica que vamos a cambiar el comportamiento de nuestro metodo
#     # En general permite no colocar los parentesis al final de la llamada
#     @property
#     def nombre(self):
#         print('Llamando metodo get nombre')
#         return self._nombre
#
#     # @nombre.setter
#     # def nombre(self, nombre):
#     #     print("Lamando metodo set nombre")
#     #     self._nombre = nombre
#
#     def mostrar_detalles(self):
#         print(f'Persona: {self._nombre} {self.apelllido} {self.edad}')
#
#
# persona1 = Persona('Carlos', "Guzman", 18)
# print(persona1.nombre)
# # persona1._nombre = "nombre" # Si realmente queremos demostrar que sabemos programar esto no se utilizara
# # persona1.nombre = 'CArlos HUmberto' # si no tenemos un metodo set asociado no se podra hacer el cambio
# print(persona1.nombre)


# CLASE 61 ENCAPSULANDO TODOS LOS ATRIBUTOS DE UNA CLASE
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         # Cuando se coloca _ significa que el atributo esta encapsulado
#         # Ejemplos _nombre esto si permitira la modificacion pero sera como una indicacion que no se debe de hacer
#         # __nombre no permitira hacer la modificacion fuera de la clase pero no es lo mas comun
#         self._nombre = nombre
#         self._apellido = apellido
#         self._edad = edad
#
#     # Decorador indica que vamos a cambiar el comportamiento de nuestro metodo
#     # En general permite no colocar los parentesis al final de la llamada
#     @property
#     def nombre(self):
#         print('Llamando metodo get nombre')
#         return self._nombre
#
#     @nombre.setter
#     def nombre(self, nombre):
#         print("Lamando metodo set nombre")
#         self._nombre = nombre
#
#     @property
#     def apellido(self):
#         return self._apellido
#
#     @apellido.setter
#     def apellido(self, apellido):
#         self._apellido = apellido
#
#     @property
#     def edad(self):
#         return self._edad
#
#     @edad.setter
#     def edad(self, edad):
#         self._edad = edad
#
#     def mostrar_detalles(self):
#         print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
#
#
# persona1 = Persona('Carlos', "Guzman", 18)
# print(persona1.nombre)
# # persona1._nombre = "nombre" # Si realmente queremos demostrar que sabemos programar esto no se utilizara
# persona1.nombre = 'CArlos HUmberto' # si no tenemos un metodo set asociado no se podra hacer el cambio
# print(persona1.nombre)
#
# persona1.apellido = "Ramirez"
# persona1.edad = 20
# persona1.nombre = "Humberto"
# persona1.mostrar_detalles()


# CLASE 62 USO DE MODULOS Y CLASES EN PYTHON
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         # Cuando se coloca _ significa que el atributo esta encapsulado
#         # Ejemplos _nombre esto si permitira la modificacion pero sera como una indicacion que no se debe de hacer
#         # __nombre no permitira hacer la modificacion fuera de la clase pero no es lo mas comun
#         self._nombre = nombre
#         self._apellido = apellido
#         self._edad = edad
#
#     # Decorador indica que vamos a cambiar el comportamiento de nuestro metodo
#     # En general permite no colocar los parentesis al final de la llamada
#     @property
#     def nombre(self):
#         return self._nombre
#
#     @nombre.setter
#     def nombre(self, nombre):
#         self._nombre = nombre
#
#     @property
#     def apellido(self):
#         return self._apellido
#
#     @apellido.setter
#     def apellido(self, apellido):
#         self._apellido = apellido
#
#     @property
#     def edad(self):
#         return self._edad
#
#     @edad.setter
#     def edad(self, edad):
#         self._edad = edad
#
#     def mostrar_detalles(self):
#         print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
#
#
# persona1 = Persona('Carlos', "Guzman", 18)
# # persona1._nombre = "nombre" # Si realmente queremos demostrar que sabemos programar esto no se utilizara
# persona1.nombre = 'CArlos HUmberto'  # si no tenemos un metodo set asociado no se podra hacer el cambio
#
# persona1.apellido = "Ramirez"
# persona1.edad = 20
# persona1.nombre = "Humberto"
# persona1.mostrar_detalles()


# CLASE 64 DESTRUCTOR DE OBJETOS EN PYTHON
class Persona:
    def __init__(self, nombre, apellido, edad):
        # Cuando se coloca _ significa que el atributo esta encapsulado
        # Ejemplos _nombre esto si permitira la modificacion pero sera como una indicacion que no se debe de hacer
        # __nombre no permitira hacer la modificacion fuera de la clase pero no es lo mas comun
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # Decorador indica que vamos a cambiar el comportamiento de nuestro metodo
    # En general permite no colocar los parentesis al final de la llamada
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    # DECONSTRUCTOR
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

if __name__ == '__main__':
    persona1 = Persona('Carlos', "Guzman", 18)
    # persona1._nombre = "nombre" # Si realmente queremos demostrar que sabemos programar esto no se utilizara
    persona1.nombre = 'CArlos HUmberto'  # si no tenemos un metodo set asociado no se podra hacer el cambio

    persona1.apellido = "Ramirez"
    persona1.edad = 20
    persona1.nombre = "Humberto"
    persona1.mostrar_detalles()

# print(__name__)  # Esto es para saber desde dode se esta ejecutando
