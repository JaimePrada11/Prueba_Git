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

    print(f"{'ID':<10} {'Nombre':<15} {'Apellido':<15} {'Correo':<25}")
    for clave, valor in Informacion.items():
        print(f"{clave:<10} {valor['Nombre']:<15} {valor['Apellido']:<15} {valor['Correo']:<25}")
