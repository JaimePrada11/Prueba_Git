from Manejo_Datos import *

def validar_cedula(cedula):
    for Categoria in Informacion.keys():
        if cedula in Categoria:
            return True
    return False