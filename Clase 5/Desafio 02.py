from data_stark import lista_personajes

def stark_normalizar_datos (lista:list):
    """
    Recorre una lista
    lista: tiene que ser una lista de diccionarios  
    """

        
   
    for elemento in lista:
        if(type(elemento) != type(float())):
            elemento["altura"] = float(elemento["altura"])
        if(type(elemento) != type(float())):
            elemento["peso"] = float(elemento["peso"])
        if(type(elemento) != type(int())):
            elemento["fuerza"] = int(elemento["fuerza"])
        
print(type(elemento))
    
