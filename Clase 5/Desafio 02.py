from data_stark import lista_personajes

#---------------0.0----------------
def stark_normalizar_datos (lista:list):
    """
    Recorre una lista y convierte al tipo de dato correcto las keys
    lista: tiene que ser una lista de diccionarios  
    """
    if len(lista_personajes) > 0:
        flag = True 
        for elemento in lista:
            if(type(elemento) != type(float())):
                elemento["altura"] = float(elemento["altura"])
                flag = False
            if(type(elemento) != type(float())):
                elemento["peso"] = float(elemento["peso"])
                flag = False
            if(type(elemento) != type(int())):
                elemento["fuerza"] = int(elemento["fuerza"])
                flag = False
        if flag == False:
            print("Datos Normalizados")
    else: 
        print("Error: Lista de héroes vacía")


stark_normalizar_datos(lista_personajes)
    
#-----------1.1-----------------------

def obtener_nombre(diccionario:dict)-> str:
    
    nombre_heroe = "Nombre: {0}".format(diccionario["nombre"])
    
    return nombre_heroe
     
print(obtener_nombre(lista_personajes[0]))
   
#------------1.2---------------------
def imprimir_dato(dato:str):
    print(dato)
    
#------------1.3---------------------
def stark_imprimir_nombres_heroes(lista:list):
    pass