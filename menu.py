from archivo_json import cargado_de_datos,guardado_de_datos
from funciones import *

cargado_de_datos()

def menu_empleados():
    print("---MENU SOLO EMPLEADOS---")
    print("#1.registro de envio\n#2.actualizar estado de un paquete\n#3.imprimir recibo")

    opcion=int(input("ingrese la opcion escogida"))

    if opcion==1:
        registro_de_envio()
    elif opcion ==2:
        actualizar_estado_envio()
    elif opcion == 3:
        imprimir_recibo()
    else:
        print("ERROR ESA OPCION NO EXISTE O HAY UN PROBLEMA INTENTE MAS TARDE")

def menu():
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
            menu_empleados
        else:
            print("Opción no válida.")

menu()