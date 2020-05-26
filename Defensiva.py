# Alejandro Corzo  
# Paulina Perez    
# El otro     
# El otro x2  
# FECHA : 20/10/2019
# SECCION
# Funciones de defensa
def Entero(opcion):
    # se verifica si se puede convertir a entero lo que ingresa el usuario
    try:
        opcion = int(opcion)
        bandera = True
    except:
        bandera = False
        
    return bandera
        
  