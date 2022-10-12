import re
import json


def cargar_json(path:str):
    with open(path, "r") as file:
        json_file = json.load(file)
        
    return json_file["results"]

#print(cargar_json("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 12/data.json"))

def mostrar(lista:list):
    for elemento in lista:
        print("Nombre: {0}| Altura: {1}| Peso: {2}| Genero: {3}"
              .format(elemento["name"],elemento["height"],elemento["mass"],elemento["gender"]))

def validar_dato(dato:str,patron:str):
    if re.match(patron,dato):
        return True
    else:
        return False

def convertir_datos(lista:list):
    flag = True
    for elemento in lista:
        if type(elemento) != type(int()):
            elemento["height"] = int(elemento["height"])
            flag = False
        if type(elemento) != type(int()):
            elemento["mass"] = int(elemento["mass"])
            flag = False

#-----------------1,3-----------------------
def buscar_minimo(lista:list,key:str):
    convertir_datos(lista)
    minimo = 0
    for i in range(len(lista)):
        if(lista[i][key] < lista[minimo][key]):
            minimo = i
    return minimo

def ordenar(lista:list,key:str):
    convertir_datos(lista)
    lista_ordenada = []
    lista_copia = lista.copy()
    while(len(lista_copia) > 0):
        minimo = buscar_minimo(lista_copia, key)
        lista_ordenada.append(lista_copia.pop(minimo))
    return lista_ordenada        

#----------------2------------------------
def buscar_personaje_genero(lista:list,genero:str):
    heroe_genero = {}
    for elemento in lista:
        if elemento["gender"] == "male" or elemento["gender"]=="female":
            heroe_genero = elemento
            break
    
    return heroe_genero

def mostrar_personaje_mas_alto_genero(lista:list,genero:str):
    convertir_datos(lista)
    personaje_alto = buscar_personaje_genero(lista, genero)
    personaje_alto["height"]= int(personaje_alto["height"])
    for elemento in lista:
        if elemento["height"] > personaje_alto["height"]:
            personaje_alto = elemento

    return personaje_alto  
        
#-----------------1---------------------------
# def buscar_max_min(lista:list,key:str,orden:str):
#     convertir_datos(lista)
#     i_min_max = 0
#     for i in range(len(lista)):
#         if(orden == "desc" and lista[i][key] > lista[i_min_max][key]) or ((orden == "asc" and lista[i][key] < lista[i_min_max][key])) :
#             i_min_max
            
#     return i_min_max

# def ordenar_lista(lista:list,key:str,orden:str):
#     convertir_datos(lista)
#     lista_ordenada = lista.copy()
#     for i in range(len(lista_ordenada)):
#         index_min_max = buscar_max_min(lista_ordenada[i:], key,orden)+i
#         lista_ordenada[i],lista_ordenada[index_min_max] = lista_ordenada[index_min_max],lista_ordenada[i]
        
#     return lista_ordenada

#------------4-----------------------

def buscar_personajes(lista:list,tipo:str):
    for elemento in lista:
        resultado = re.search(tipo,elemento["name"],re.IGNORECASE)
        if resultado :
            nombre = elemento["name"]
            print("PJ: {0} | Altura: {1}| Peso: {2}| Genero: {3}"
                  .format(nombre,elemento["height"],elemento["mass"],elemento["gender"]))


#--------------5--------------------
def exportar_csv(lista:list,path:str):
    with open(path, "w") as file:
        for elemento in lista:
            file.write("Nombre: {0}| Altura: {1}| Peso: {2}| Genero: {3}\n"
              .format(elemento["name"],elemento["height"],elemento["mass"],elemento["gender"]))