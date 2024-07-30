from Manejo_Datos import *
from Validaciones import *


def Registro():
    cargar_datos()
    print("************************************************************")
    print("                   REGISTRO ")
    print("************************************************************\n")
    
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

def reporte():
    cargar_datos()
    print("************************************************************")
    print("                   REPORTES")
    print("************************************************************\n")

    print(f"{'ID':<10} {'Nombre':<15} {'Apellido':<15} {'Correo':<20}")
    print("-" * 60)
    for clave, valor in Informacion.items():
        print(f"{clave:<10} {valor['Nombre']:<15} {valor['Apellido']:<15} {valor['Correo']:<20}")
    print("-" * 60)


def buscar_id():
    cargar_datos()
    print("************************************************************")
    print("                   REPORTE USUARIO ESPECIFICO")
    print("************************************************************\n")

    ID= input("Ingresa la cedula:  ")
    if ID not in Informacion:
        print("*" * 60)
        print("El usuario con la cédula ingresada no existe. \nPor favor, intente de nuevo")
        print("*" * 60)
        return
    else:
        print(f"{'ID':<10} {'Nombre':<15} {'Apellido':<15} {'Correo':<20}")
        print("-" * 60)
        usuario = Informacion[ID]
        print(f"{ID:<10} {usuario['Nombre']:<15} {usuario['Apellido']:<15} {usuario['Correo']:<20}")
        print("-" * 60)

