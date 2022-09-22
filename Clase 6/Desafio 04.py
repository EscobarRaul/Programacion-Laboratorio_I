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
        return "N/A"

# for heroe in lista_personajes:
#     print(extraer_iniciales(heroe["nombre"]))

#-----------------------1.2-----------------------------
def definir_iniciales_nombre(heroe:dict):
    retorno = True
    
    if (type(heroe) == dict and "nombre" in heroe.keys()):
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        #print(heroe["iniciales"])
        
    else:
        retorno = False

    return retorno
    
# for heroe in lista_personajes:
#     print(definir_iniciales_nombre(heroe))
    
#--------------------------1.3-----------------------------
def agregar_iniciales_nombre(lista_heroes:list):
    retorno = True
    if (type(lista_heroes) == list and len(lista_heroes) > 0):
        for heroe in lista_heroes:
            definir_iniciales_nombre(heroe)
            
    else:
        retorno = False
        print("El origen de datos no contiene el formato correcto")

    return retorno

#for heroe in lista_personajes:
# agregar_iniciales_nombre(lista_personajes)
# print(lista_personajes)
#-------------------1.4-------------------------
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    if type(lista_heroes) == list and len(lista_heroes) > 0:
        agregar_iniciales_nombre(lista_heroes)
        for heroe in lista_heroes:
            print("*{0}({1})".format(heroe["nombre"],heroe["iniciales"]))
        
#stark_imprimir_nombres_con_iniciales(lista_personajes)

#---------------------2.1--------------------------
def generar_codigo_heroe(id_heroe:int,genero_heroe:str):
    if type(id_heroe) == int and len(genero_heroe)>0:
        id_heroe = str(id_heroe)
        if genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB":
            mensaje = "{0}-{1}".format(genero_heroe,id_heroe.zfill(8))

            return mensaje
        else:
            return "N/A"
    else:
        return "N/A"

#print(generar_codigo_heroe(1,"M"))

#---------------------2.2-------------------
def agregar_codigo_heroe(heroe:dict,id_heroe:int):
    if len(heroe) > 0 and len(generar_codigo_heroe(id_heroe,heroe["genero"])) == 10: 
        heroe["codigo_heroe"] = generar_codigo_heroe(id_heroe,heroe["genero"])

        return True
    else:
        return False

# print(agregar_codigo_heroe(lista_personajes[10],10))
# print(lista_personajes[10])

#-------------------2.3-------------------
def stark_generar_codigos_heroes(lista_heroes:list):

    for heroe in lista_heroes:
        heroe = agregar_codigo_heroe(heroe,)



stark_generar_codigos_heroes(lista_personajes)