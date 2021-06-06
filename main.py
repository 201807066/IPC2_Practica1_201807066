import os, sys, time
import funciones

def cls():
    os.system('cls')

def menuPrincipal():
    cls()
    while True:
        print("************* PRACTICA 1 *************\n")
        print("Menú Principal")
        print("1) Ingresar nuevo contacto")
        print("2) Buscar contacto")
        print("3) Visualizar agenda")
        print("4) Mostrar datos del estudiante")
        print("5) Salir")
        opc = input("\nOpción a realizar: ")

        if opc == "1":
            funciones.nuevoContacto()
            menuPrincipal()
            break
        elif opc == "2":
            funciones.buscar()
            menuPrincipal()
            break
        elif opc == "3":
            funciones.visualizarAgenda()
            menuPrincipal()
            break
        elif opc == "4":
            cls()
            print("****************************************")
            print("**** Introducción a la Programación ****")
            print("****        y Computación 2         ****")
            print("****          Sección N             ****")
            print("****                                ****")
            print("****      Ciencias y sistemas       ****")
            print("****   Brayan Andrés Cholotio Tum   ****")
            print("****           201807066            ****")
            print("****************************************\n")
            input("Presione cualquier tecla para continuar...")
            menuPrincipal()
            cls()
            break
        elif opc == "5":
            cls()
            print("Saliendo del sistema...")
            time.sleep(2)
            os.system("exit")
            break
        else:
            print("Opción incorrecta...")
            time.sleep(1)
            cls() 

menuPrincipal()