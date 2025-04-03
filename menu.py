'''importar las funciones y las funciones para que funcione los json'''
from archivo_json import cargado_de_datos,guardado_de_datos
from funciones import *

cargado_de_datos()

def menu_empleados():
    '''menu para solo empleados esto dejara alos empleados hecer cosas que no se pueden hacer con el menu principal'''
    print("\n---MENU SOLO EMPLEADOS---")
    print("#1.registro de envio\n#2.actualizar estado de un paquete\n#3.imprimir recibo\n#4. salir")

    opcion=int(input("ingrese la opcion escogida: "))

    if opcion==1:
        registro_de_envio()
        guardado_de_datos()
    elif opcion ==2:
        actualizar_estado_envio()
        guardado_de_datos()
    elif opcion == 3:
        imprimir_recibo()
    elif opcion == 4:
        print("saliendo del menu solo de empleados")
        menu()
    else:
        print("ERROR ESA OPCION NO EXISTE O HAY UN PROBLEMA INTENTE MAS TARDE")

def menu():
    '''menu principal para que los usuarios lo utilicen'''
    while True:
        print("\n--- Menú ---")
        print("1. Registrar cliente")
        print("2. Seguir envío")
        print("3. Imprimir recibo")
        print("4. Actualizar información del cliente")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registro_usuario()
            guardado_de_datos()
        elif opcion == 2:
            seguir_envio()  
        elif opcion == 3:
            imprimir_recibo()
        elif opcion == 4:
            actualizar_informacion_cliente()
            guardado_de_datos()
        elif opcion == 5:
            guardado_de_datos()
            print("Saliendo del programa.")
            break
        elif opcion == 12345:
            menu_empleados()
        else:
            print("Opción no válida.")

menu()