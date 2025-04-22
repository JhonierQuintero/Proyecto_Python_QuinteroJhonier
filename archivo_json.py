'''se importa la libreria json y del modulo funciones los dos diccionarios'''
import json
from funciones import clientes, envios

def guardado_de_datos():
    """Guarda los diccionarios de clientes y envíos en un archivo JSON."""
    with open("./proyecto_gestion_de_envios_y_logistica/datos.json", "w",encoding='utf 8') as f:
        datos = {
            "clientes": clientes,
            "envios": envios
        }
        json.dump(datos, f)
    print("Datos guardados exitosamente.")

def cargado_de_datos():
    """Carga los datos desde el archivo JSON o inicializa diccionarios vacíos si no existe."""
    try:
        with open("./proyecto_gestion_de_envios_y_logistica/datos.json", "r", encoding='utf 8') as f:
            datos = json.load(f)
            clientes.update(datos["clientes"])
            envios.update(datos["envios"])
        print("Datos cargados exitosamente.")
    except FileNotFoundError:
        print("Archivo de datos no encontrado. Iniciando con datos vacíos.")