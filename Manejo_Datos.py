import json 
import csv

Informacion = {}

Ruta = "Data_Base/Informacion.json" 
Ruta_csv = "Data_Base/Informacion.csv" 

def guardar_datos():
    try:
        with open(Ruta, "w", encoding='utf-8') as file:
            json.dump(Informacion, file, indent=4, ensure_ascii=False  )
    except Exception as e:
        print(f"Error {e}")
        registrar_error(e)


def cargar_datos():
    try:
        with open(Ruta, "r", encoding='utf-8') as archivo:
            Informacion.update(json.load(archivo))
    except Exception as e:
        print(f"Error al cargar datos {e}")
        registrar_error(e)


def guardar_csv():
    try:
        with open(Ruta_csv, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Apellido", "Correo", "Cel"])  # Cabecera del CSV
            for id, datos in Informacion.items():
                writer.writerow([id, datos["Nombre"], datos["Apellido"], datos["Correo"], datos["Cel"]])
    except Exception as e:
        print(f"Error al cargar datos {e}")
        registrar_error(e)


def cargar_csv():
    global Informacion
    try:
        with open(Ruta_csv, "r", encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id = row["ID"]
                Informacion[id] = {
                    "Nombre": row["Nombre"],
                    "Apellido": row["Apellido"],
                    "Correo": row["Correo"],
                    "Cel": row["Cel"]
                }
    except Exception as e:
         print(f"Error al cargar datos {e}")
         registrar_error(e)


import datetime

Ruta_errores = "Data_Base/errores.txt"

def registrar_error(mensaje_error):
    try:
        with open(Ruta_errores, "a", encoding='utf-8') as file:
            # Obtiene la fecha y hora actual
            fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Escribe el mensaje de error con la fecha y hora
            file.write(f"{fecha_hora} - ERROR: {mensaje_error}\n")
    except Exception as e:
        print(f"Error al registrar el error en el archivo: {e}")

