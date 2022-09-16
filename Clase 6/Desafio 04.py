from data_stark import lista_personajes
import re

#-----------------1.1--------------------------
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

#-----------------------1.2-----------------------------
def definir_iniciales_nombre(heroe:dict):
    retorno = True
    
    if (type(heroe) == dict ): #and type(heroe) == heroe["nombre"] NO PUEDO VALIDAR EL NOMBRE
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        print(heroe["iniciales"])
        
    else:
        retorno = False

    return retorno
    
for heroe in lista_personajes:
    print(definir_iniciales_nombre(heroe))
    
#--------------------------1.3-----------------------------
def agregar_iniciales_nombre(lista_heroes:list):
    retorno = True
    if (type(lista_heroes) == list and len(lista_heroes) > 0):
        for heroe in lista_heroes:
            heroe = definir_iniciales_nombre(heroe)
            #print(heroe)
    else:
        retorno = False
        print("El origen de datos no contiene el formato correcto")

    return retorno

# for heroe in lista_personajes:
#     print(agregar_iniciales_nombre(lista_personajes))