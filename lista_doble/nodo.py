class Nodo(object):

    def __init__(self, nombre = None, apellido = None, telefono = None, siguiente = None, anterior = None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.siguiente = siguiente
        self.anterior = anterior