from Manejo_Datos import *


def Registro():
    cargar_datos()

    usuario= {} 
    ID = input("Ingresa el ID: ")
    usuario["Nombre"] = input("Ingresa el nombre:  ").upper()
    usuario["Apellido"] = input("Ingresa el apellido:  ").upper()
    usuario["Correo"] = input("Ingresa el correo:  ").upper()
    usuario["Cel"] = input("Ingresa el celular:  ")
    Informacion[ID] = usuario
    guardar_datos()

