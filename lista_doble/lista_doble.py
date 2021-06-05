from lista_doble.nodo import Nodo

class ListaDoble():

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

#Metodo que agrega al final de la lista doble enlazada
    def agregar(self, nombre, apellido, telefono):
        if self.vacia():
            self.primero = self.ultimo = Nodo(nombre, apellido, telefono)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = None(nombre, apellido, telefono)
            self.ultimo.anterior = aux
        self.size += 1

#recorrer la lista de inicio a fin
    def recorrer_inicio(self):
        aux=self.primero
        while aux:
            print("Nombre: " + aux.nombre)
            print("Apellido: " + aux.apellido)
            print("Teléfono: " + aux.telefono)
            aux=aux.siguiente
        input()