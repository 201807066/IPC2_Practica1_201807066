import os, sys, time
from lista_doble.nodo import Nodo
from graphviz import Digraph


class ListaDoble():

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    #Revisamos si tenemos nodos en la lista
    def vacia(self):
        return self.primero == None

    #Metodo que agrega al final de la lista doble enlazada
    def agregar_fin(self, name, lastname, cel):
        if self.vacia():
            self.primero = self.ultimo = Nodo(name, lastname, cel)
            print("\nEl contacto se ha agregado exitosamente.")
            input("\n--> Presione cualquier tecla para continuar...")
        else:
            temp = self.primero

            if lastname < self.primero.apellido:
                nodo1 = Nodo(name, lastname, cel)
                aux = self.primero
                nodo1.siguiente = aux
                self.primero = nodo1
                aux.anterior = nodo1
                print("\nEl contacto se ha agregado exitosamente.")
                input("\n--> Presione cualquier tecla para continuar...")
                self.size += 1
                return

            if self.primero.siguiente != None:
                if lastname < self.primero.siguiente.apellido:
                    nodo1 = Nodo(name, lastname, cel)
                    aux = self.primero.siguiente
                    nodo1.siguiente = aux
                    self.primero.siguiente = nodo1
                    aux.anterior = nodo1
                    print("\nEl contacto se ha agregado exitosamente.")
                    input("\n--> Presione cualquier tecla para continuar...")
                    self.size += 1
                    return

            #No es mayor a la cabeza ni a la siguiente de la cabeza
            while temp != None:
                if lastname < temp.apellido:
                    nodo1 = Nodo(name, lastname, cel)
                    aux = temp
                    nodo1.siguiente = aux
                    aux.anterior.siguiente = nodo1
                    nodo1.anterior = aux.anterior
                    print("\nEl contacto se ha agregado exitosamente.")
                    input("\n--> Presione cualquier tecla para continuar...")
                    self.size += 1
                    return
                    
                temp = temp.siguiente

            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(name, lastname, cel)
            self.ultimo.anterior = aux
            print("\nEl contacto se ha agregado exitosamente.")
            input("\n--> Presione cualquier tecla para continuar...")
        self.size += 1

    #Comprobamos que no se repita el número en la lista
    def agregar(self, nombre, apellido, telefono):
        aux = self.primero
        while aux != None:
            if aux.telefono == telefono:
                print("\nEl número de teléfono ya ha sido registrado -> " + telefono)
                input("\n--> Presione cualquier tecla para continuar...")
                return
            aux = aux.siguiente

        self.agregar_fin(nombre, apellido, telefono)

    #recorrer la lista
    def mostrar(self):
        aux=self.primero
        while aux:
            print("Nombre: " + aux.nombre)
            print("Apellido: " + aux.apellido)
            print("Teléfono: " + aux.telefono + "\n")
            aux=aux.siguiente
    
    def buscar_numero(self, numero):
        aux = self.primero
        

        while aux != None:
            if aux.telefono == numero:
                print("\nNombre: " + aux.nombre)
                print("Apellido: " + aux.apellido)
                print("Teléfono: " + aux.telefono + "\n")
                input("\nPresione cualquier tecla para continuar... ")
                return True
        
            aux = aux.siguiente
        print("\nEl número de teléfono no existe...")
        return False
            

    def Size(self):
        print("Cantidad de contactos registrados: " + str(self.size))

    #Imprime la lita enlazada
    def imagen_dot(ListaDoble):
        f = Digraph(format = "png", name = "salida")
        f.attr(size = "8,5")

        aux=ListaDoble.primero
        cont = 0
        while aux:
            f.node(str(cont), " Nombre: " + aux.nombre + "\nApellido: " + aux.apellido + "\nTeléfono: " + aux.telefono)
            cont += 1
            aux=aux.siguiente
        
        f.node('-1', 'Agenda')
        f.node(str(cont), 'Fin Agenda')
        cont = 0
        aux=ListaDoble.primero
        while aux:    
            f.edge(str(cont), str(cont - 1 ))
            f.edge(str(cont), str(cont + 1 ))
            cont += 1
            aux = aux.siguiente

        f.render()
        os.system('salida.gv.png')

        #edge[dir="both"]