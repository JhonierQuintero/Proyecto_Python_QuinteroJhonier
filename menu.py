'''importar las funciones y las funciones para que funcione los json'''
from archivo_json import cargado_de_datos,guardado_de_datos
from funciones import *

cargado_de_datos()

def menu_empleados():
    '''menu para solo empleados esto dejara alos empleados hecer cosas que no se pueden hacer con el menu principal'''

    while True: 

        print("\n---MENU EMPLEADOS---")
        print("#1.registro de envio\n#2.registro de clientes\n#3.actualizar informacion del cliente\n#4.actualizar estado de un paquete\n#5.imprimir clientes\n#6.imprimir envios\n#7. salir")

        opcion=int(input("ingrese la opcion escogida: "))

        if opcion==1:
            registro_de_envio()
            guardado_de_datos()
        elif opcion == 2:
            registro_usuario()
            guardado_de_datos()
        elif opcion == 3:
            actualizar_informacion_cliente()
        elif opcion ==4:
            actualizar_estado_envio()
            guardado_de_datos()
        elif opcion == 5:
            imprimir_clientes()
        elif opcion == 6:
            imprimir_envios() 
        elif opcion == 7:
            print("saliendo del menu solo de empleados")
            break
        else:
            print("ERROR ESA OPCION NO EXISTE O HAY UN PROBLEMA INTENTE MAS TARDE")

def menu_administrador():
    while True:
        print("\n=== Menú del Administrador ===")
        print("#1. Registrar un cliente")
        print("#2. Registrar un envío")
        print("#3. Imprimir todos los clientes")
        print("#4. Imprimir todos los envíos")
        print("#5. Informe de volumen de envíos")
        print("#6. actualizar informacion cliente")
        print("#7. salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            registro_usuario()
            guardado_de_datos()
        elif opcion == 2:
            registro_de_envio()
            guardado_de_datos()
        elif opcion == 3:
            imprimir_clientes()
        elif opcion == 4:
            imprimir_envios()
        elif opcion == 5:
            dias=int(input("ingrese el numero de dias que quiera el informe: "))
            informe_volumen_envios(dias)
        elif opcion == 6:
            actualizar_informacion_cliente()
        elif opcion == 7:
            print("saliendo del menu de abministrador")
            guardado_de_datos()
            break
        else:
            print("ERROR ESA OPCION NO EXISTE O HAY UN PROBLEMA INTENTE MAS TARDE")

def menu():
    '''menu principal para que los usuarios lo utilicen'''
    while True:
        print("\n--- Menú ---")
        print("#1. Registrarce")
        print("#2. Seguir envío")
        print("#3. Imprimir recibo del envio")
        print("#4. Actualizar tu información")
        print("#5. Salir")
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
        elif opcion == 123456789:
            menu_administrador()
        else:
            print("Opción no válida.")

menu()