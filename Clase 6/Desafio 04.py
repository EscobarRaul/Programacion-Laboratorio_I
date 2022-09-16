from data_stark import lista_personajes
import re

def extraer_iniciales(nombre_heroe:str)-> str:
    
    if len(nombre_heroe) > 0:
        nombre_heroe = nombre_heroe.replace("The ", "")
        nombre_heroe = nombre_heroe.replace("the ", "")
        nombre_heroe = nombre_heroe.replace("-", " ")
        nombre_heroe = nombre_heroe.upper()
        nombre_heroe = nombre_heroe.strip()
        
        lista_nombre = nombre_heroe.split(" ")
        
        iniciales = ""
        for nombre in lista_nombre:
            nombre = nombre[0:1]
            iniciales += "{0}.".format(nombre)
            
        return iniciales
        
    else:
        if nombre_heroe == "":
            return "N/A"

# for heroe in lista_personajes:
#     print(extraer_iniciales(heroe["nombre"]))
 
"""
    La función devuelve un nuevo string con las iniciales del 
    nombre del personaje
"""
    # if nombre_heroe == "":
    #     return "N/A"
    # else:
    #     if len(nombre_heroe) > 0 :
    #         if nombre_heroe.count("the") > 0 :
    #             nombre_heroe = nombre_heroe.replace("the ", "")
            
    #         if nombre_heroe.count("-") > 0 :
    #             nombre_heroe = nombre_heroe.replace("-", "")

    #         lista1 = nombre_heroe.split(" ")
    #         print(lista1)
            
    #         iniciales = ""
    #         for nombre in lista1:
    #             nombre = nombre[0:1]
    #             nombre = nombre.upper()
    #             iniciales += "{0}.".format(nombre)
            
    #         return iniciales
                   
#print(extraer_iniciales("")) 

def definir_iniciales_nombre(heroe:dict):
    retorno = True
    
    if (type(heroe) == dict):
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        #print(heroe["iniciales"])
        
    else:
        retorno = False

    return retorno
    
for heroe in lista_personajes:
    print(definir_iniciales_nombre(heroe))
    
