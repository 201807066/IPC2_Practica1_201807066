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

    if nombre == "" or apellido == "":
        print("No es un nombre valido")
        time.sleep(1)
        nuevoContacto()
    else:
        if len(telefono) == 8:
            lista.agregar(nombre.capitalize(), apellido.capitalize(), telefono)
        else:
            print("La cantidad de números no corresponde a un número telefónico valido...")
            time.sleep(1)
            nuevoContacto()
        

#Busqueda de contacto por medio del numero
def buscar():
    cls()
    print("********** Buscar Contacto **********\n")

    if lista.vacia():
        print("No hay contactos agregados")
        time.sleep(1)
    else:
        telefono = input("Ingrese el número por buscar: ")
        if len(telefono) == 8:
            if lista.buscar_numero(telefono) == True:
                print("Muestra el contacto")
            else:
                x = input("¿Desea agregarlo? Si/No: ")
                if x.lower() == "si":
                    cls()
                    print("********** Nuevo Contacto **********\n")
                    print("Número de teléfono: " + telefono)
                    nombre = input("\nIngrese nombre: ")
                    apellido = input("Ingrese apellido: ")
                    print("Número de teléfono: " + telefono)
            
                    lista.agregar(nombre.capitalize(), apellido.capitalize(), telefono)
                else:
                    pass
        else:
            print("La cantidad de números no corresponde a un número telefónico valido...")
            time.sleep(1)
            buscar()


#Metodo para generar imagen
def visualizarAgenda():
    cls()
    if lista.vacia():
        print("*"*60 + "\n")
        print("Para generar una grafica debe agregar un nuevo contacto...\n")
        time.sleep(1.5)
    else:
        lista.Size()
        ListaDoble.imagen_dot(lista)
        input()

