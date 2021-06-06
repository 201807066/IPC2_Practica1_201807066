import os, sys, time
from lista_doble.lista_doble import ListaDoble


lista = ListaDoble()

def cls():
    os.system("cls")

#Agregar un nuevo contacto a la agenda
def nuevoContacto():
    cls()
    print("********** Nuevo Contacto **********\n")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    telefono = input("Ingrese número de teléfono: ")

    if len(telefono) >= 9:
        print("La cantidad de números es incorrecto")
        time.sleep(1)
        nuevoContacto()
    else:
        lista.agregar(nombre, apellido, telefono)

#Busqueda de contacto por medio del numero
def buscar():
    cls()
    print("********** Buscar Contacto **********\n")

    if lista.vacia():
        print("No hay contactos agregados")
        time.sleep(1)
    else:
        lista.buscar_numero()
        input()
    
#Metodo para generar imagen
def visualizarAgenda():
    cls()
    if lista.vacia():
        print("*"*60 + "\n")
        print("Para generar una grafica debe agregar un nuevo contacto...\n")
        time.sleep(1.5)
    else:
        lista.mostrar()
        lista.Size()
        ListaDoble.imagen_dot()
        input()

