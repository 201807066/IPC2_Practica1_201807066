import os, sys, time
from lista_doble.nodo import Nodo

class ListaDoble():

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

#Metodo que agrega al final de la lista doble enlazada
    def agregar_fin(self, name, lastname, cel):
        if self.vacia():
            self.primero = self.ultimo = Nodo(name, lastname, cel)
            print("\nEl contacto se ha agregado exitosamente.")
            input("\n--> Presione cualquier tecla para continuar...")
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(name, lastname, cel)
            self.ultimo.anterior = aux
            print("\nEl contacto se ha agregado exitosamente.")
            input("\n--> Presione cualquier tecla para continuar...")
        self.size += 1

    def agregar(self, nombre, apellido, telefono):
        aux = self.primero
        while aux != None:
            if aux.telefono == telefono:
                print("\nEl número de teléfono ya ha sido registrado -> " + telefono)
                input("\n--> Presione cualquier tecla para continuar...")
                return
            aux = aux.siguiente

        self.agregar_fin(nombre, apellido, telefono)



#recorrer la lista de inicio a fin
    def mostrar(self):
        aux=self.primero
        while aux:
            print("Nombre: " + aux.nombre)
            print("Apellido: " + aux.apellido)
            print("Teléfono: " + aux.telefono + "\n")
            aux=aux.siguiente
    
    def buscar_numero(self):
        aux = self.primero
        numero = input("Ingrese el número por buscar: ")

        while aux != None:
            if aux.telefono == numero:
                print("\nNombre: " + aux.nombre)
                print("Apellido: " + aux.apellido)
                print("Teléfono: " + aux.telefono + "\n")
            aux = aux.siguiente
            

    def Size(self):
        print(self.size)

    def imagen_dot():
        f = open('salida.dot', 'w', encoding='utf-8')
        f.write("digraph agenda{\n")
        f.write('')

#Codigo 

        f.write('}')
        f.close()

        os.system('dot -Tpng salida.dot -o salida.png')
        print('Generando imagen...')
        time.sleep(1.5)
        os.system('salida.png')



