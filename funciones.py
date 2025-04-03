from datetime import datetime, timedelta
from archivo_json import *
import random
clientes={}
envios={}
ESTADOS_VALIDOS = ["Recibido", "En Transito", "En Ciudad Destino", "En Bodega De La Transportadora", "En Reparto", "Entregado"]

def registro_usuario():
    nombres=str(input("ingrese sus nombres:\n")).title()
    apellidos=str(input("ingrese su apellidos:\n")).title()
    numero_identificacion=(input("ingrese su # de identificacion:\n"))
    while True:
        print("elige una opcion segun su tipo de identificacion\n#1.CC\n#2.TI\n#3.CE")
        tipo_identificacion=int(input("ingrese su tipo de identificacion: "))
        
        if tipo_identificacion == 1:
            tipo_identificacion="CC"
            break
        elif tipo_identificacion== 2:
            tipo_identificacion="TI"
            break  
        elif tipo_identificacion ==3:
            tipo_identificacion="CE" 
            break
        else: 
            print("error esa opcion no es valida intente de nuevo\n")
           
    direccion=str(input("ingrese su direccion de residencia:\n")).title()
    barrio_residencia=str(input("ingrese el nombre de su barrio de residencia:\n")).title()
    telefono_fijo=(input("ingrese su telefono fijo:\n"))
    telefono_celular=(input("ingrese su numero celular:\n"))
    
    cliente={
        "nombres": nombres,
        "apellidos": apellidos ,
        "numero de identificacion": numero_identificacion,
        "tipo de identificacion":tipo_identificacion,
        "direccion":direccion,
        "barrio de residencia": barrio_residencia,
        "telefono fijo": telefono_fijo,
        "telefono celular": telefono_celular
        }
    
    clientes[numero_identificacion]=cliente

    print("cliente registrado exitosamente")
    
def registro_de_envio():
    fecha_envio=datetime.now().strftime('%d-%m-%Y')
    hora_envio=datetime.now().strftime('%H:%M:%S')
    nombre_dest = input("Nombre del destinatario:\n").title()
    direccion_dest = input("Dirección del destinatario:\n").title()
    telefono_dest = input("Teléfono del destinatario:\n")
    ciudad_dest = input("Ciudad del destinatario:\n").title()
    barrio_dest = input("Barrio del destinatario:\n").title()
    destinatario = {
        "nombre": nombre_dest,
        "direccion": direccion_dest,
        "telefono": telefono_dest,
        "ciudad": ciudad_dest,
        "barrio": barrio_dest
    }
    remitente_id = input("Número de identificación del remitente:\n")
    if remitente_id not in clientes:
        print("El remitente no está registrado.")
        return
    numero_guia = random.randint(1000000,10000000)
    envio = {
        "fecha": fecha_envio,
        "hora": hora_envio,
        "destinatario": destinatario,
        "remitente_id": remitente_id,
        "numero_guia": numero_guia,
        "estado": "Recibido"
    }
    envios[numero_guia] = envio
    print(f"Envío registrado con número de guía: {numero_guia}")

def seguir_envio():
    """Busca un envío por su número de guía y muestra su información."""
    numero_guia = input("Ingrese el número de guía: ")
    if numero_guia in envios:
        envio = envios[numero_guia]
        print(f"Envío {numero_guia}:")
        print(f"Fecha: {envio['fecha']}")
        print(f"Hora: {envio['hora']}")
        print(f"Destinatario: {envio['destinatario']['nombre']} - {envio['destinatario']['ciudad']}, {envio['destinatario']['barrio']}")
        print(f"Remitente: {clientes[envio['remitente_id']]['nombres']} {clientes[envio['remitente_id']]['apellidos']} - ID: {envio['remitente_id']}")
        print(f"Estado: {envio['estado']}")
    else:
        print("Número de guía no encontrado.")

def actualizar_estado_envio():
    """Permite a los trabajadores actualizar el estado de un envío."""
    numero_guia = input("Ingrese el número de guía del envío: ")
    if numero_guia in envios:
        print("Estados válidos:")
        for i, estado in enumerate(ESTADOS_VALIDOS, 1):
            print(f"{i}. {estado}")
        try:
            seleccion = int(input("Seleccione el nuevo estado (número): "))
            if 1 <= seleccion <= len(ESTADOS_VALIDOS):
                nuevo_estado = ESTADOS_VALIDOS[seleccion - 1]
                envios[numero_guia]['estado'] = nuevo_estado
                print(f"Estado actualizado a '{nuevo_estado}' para el envío {numero_guia}.")
            else:
                print("Selección fuera de rango.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
    else:
        print("Número de guía no encontrado.")
