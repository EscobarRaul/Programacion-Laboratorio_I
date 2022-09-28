import json
import re
"""
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "altura": 79.35,
    "peso": 18.45,
    "fuerza": 2,
    "inteligencia": ""
"""
def cargar_json(path:str):
    with open(path, "r") as file:
        json_file = json.load(file)
        
    return json_file["heroes"]

#print(cargar_json("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 11/Simulacro_Parcial/data_stark (1).json"))

def validar_dato_ingresado(texto_usuario:str)-> int:
    dato_ingresado = input(texto_usuario)
    dato_validado = re.match("^[1-7]{1}$", dato_ingresado)
    return int(dato_validado)
    

def mostrar(lista:list):
    for elemento in lista:
        print("Nombre: {0}| Altura: {1}| Peso: {2}| Fuerza: {3}".format(elemento["nombre"],elemento["altura"],elemento["peso"],elemento["fuerza"]))
        

def buscar_min_max(lista:list,key:str,orden:str):
    i_min_max = 0
    for i in range(len(lista)):
        if orden == "asc" and lista[i][key] > lista[i_min_max][key]:
            i_min_max = i
        if orden == "desc" and lista[i][key] < lista[i_min_max][key]:
            i_min_max
            
    return i_min_max

def ordenar_lista(lista:list,key:str,orden:str):
    lista_ordenada = lista.copy()
    for i in range(len(lista_ordenada)):
        index_min_max = buscar_min_max(lista_ordenada[i:],key,orden)+i
        lista_ordenada[i],lista_ordenada[index_min_max] = lista_ordenada[index_min_max],lista_ordenada[i]

    return lista_ordenada