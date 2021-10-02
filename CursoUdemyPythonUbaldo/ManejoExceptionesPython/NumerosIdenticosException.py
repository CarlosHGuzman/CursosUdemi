# CLASE 92 CREACION DE CLAESE DE EXCEPCION PERSONALIZADAS
class NumerosIdenticosException(Exception):
    def __init__(self, mensaje):
        self.message = mensaje