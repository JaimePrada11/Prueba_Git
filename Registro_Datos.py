from Manejo_Datos import *
from Validaciones import *


def Registro():
    cargar_datos()

    usuario= {} 
    ID = input("Ingresa el ID: ")
    if not validar_cedula(ID):
        usuario["Nombre"] = input("Ingresa el nombre:  ").upper()
        usuario["Apellido"] = input("Ingresa el apellido:  ").upper()
        usuario["Correo"] = input("Ingresa el correo:  ").upper()
        usuario["Cel"] = input("Ingresa el celular:  ")
        Informacion[ID] = usuario
    else:
        print("La cédula ya existe.")
    guardar_datos()

Registro()