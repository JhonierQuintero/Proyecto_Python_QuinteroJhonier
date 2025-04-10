# Sistema de Gestión de Envíos y Logística

Este proyecto es un sistema desarrollado en Python para la gestión de envíos y logística. Permite a los usuarios registrarse, realizar el seguimiento de sus envíos, imprimir recibos y actualizar su información. Además, ofrece funcionalidades exclusivas para administradores, como ver el volumen de envíos en un período determinado e imprimir listados completos de envíos y usuarios.

## Estructura del Proyecto

El proyecto está organizado en tres carpetas principales:

- **`/json_archivos`**: Contiene los módulos encargados de la creación y lectura de archivos JSON, gestionando la persistencia de datos como la información de usuarios y envíos.
- **`/funciones`**: Incluye todas las funciones que implementan la lógica del proyecto, como el registro de usuarios, el seguimiento de envíos, entre otros.
- **`/menus`**: Alberga los menús interactivos para los empleados, con un menú normal y un menú de administrador, que permiten acceder a las diferentes funcionalidades del sistema.

## Instalación y Requisitos

Para utilizar este sistema, necesitas lo siguiente:

- **Python 3.10.**: El proyecto está desarrollado en Python y requiere esta versión.
- No se necesitan bibliotecas externas; solo se utilizan módulos estándar de Python.

### Pasos para la instalación:

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <https://github.com/JhonierQuintero/Proyecto_Python_QuinteroJhonier>
   ```
2. Asegúrate de tener Python 3.x instalado. Puedes verificarlo con:
   ```bash
   python --version
   ```
3. Navega al directorio del proyecto:
   ```bash
   cd <proyecto_gestion_de_envios_y_logistica>
   ```

## Uso del Sistema

1. Ejecuta el archivo principal (por ejemplo, `menu.py`) desde la raíz del proyecto:
   ```bash
   python menu.py
   ```
2. Selecciona el tipo de usuario: empleado normal o administrador.
3. Dependiendo de tu elección, se mostrará el menú correspondiente con las opciones disponibles.

## Funcionalidades Principales

El sistema ofrece las siguientes funcionalidades:

- **Registro de Usuarios**: Permite a nuevos usuarios registrarse en el sistema proporcionando su información básica.
- **Seguimiento de Envíos**: Los usuarios pueden consultar el estado de sus envíos ingresando un código de seguimiento.
- **Impresión de Recibos**: Genera e imprime recibos asociados a los envíos realizados.
- **Actualización de Información**: Los usuarios pueden modificar su información personal registrada en el sistema.
- **Ver Volumen de Envíos**: Los administradores pueden visualizar la cantidad de envíos procesados en un período de tiempo específico (por ejemplo, x días).
- **Imprimir Todos los Envíos y Usuarios**: Los administradores tienen la opción de generar e imprimir listados completos de todos los envíos y usuarios registrados.

## Créditos

Este proyecto fue desarrollado por [JhonierQuintero], quien se encargó del diseño, implementación y testing del sistema.
