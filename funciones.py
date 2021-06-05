import os, sys, time
from lista_doble.lista_doble import ListaDoble


lista = ListaDoble()

def cls():
    os.system("cls")

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
        print("El contacto se ha agregado exitosamente")
        time.sleep(1)


def mostrarContacto():
    cls()
    if lista.vacia():
        print("No se han guardado contactos en la agenda")
    else:
        lista.recorrer_inicio()

