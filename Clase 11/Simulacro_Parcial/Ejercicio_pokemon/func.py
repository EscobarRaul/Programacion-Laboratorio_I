"""
            "id": 1,
			"nombre": "bulbasaur",
            "tipo": ["planta"],
            "evoluciones": ["ivysaur", "venusaur"],
			"poder": 4,
			"fortaleza":["agua"],
			"debilidad":["fuego"]
"""

import json
import re


def cargar_json(path:str):
    with open(path, "r") as file:
        json_file = json.load(file)
        
    return json_file["pokemones"]

#print(cargar_json("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 11/Simulacro_Parcial/Ejercicio_pokemon/pokedex.json"))

def mostrar(lista:list):
    for elemento in lista:
        tipo = ", ".join(elemento["tipo"])
        evo = ", ".join(elemento["evoluciones"])
        fort = ", ".join(elemento["fortaleza"])
        deb = ", ".join(elemento["debilidad"]) 
        
        print("ID: {0} |Nombre: {1} |Tipo: {2} |Evoluciones: {3} |Poder: {4} |Fortaleza: {5} |Debilidad: {6}"
        .format(elemento["id"],elemento["nombre"],tipo,evo,elemento["poder"],fort,deb))
        
        
def validar_dato_ingresado(texto_usuario:str,patron:str)-> bool:
    if re.match(patron, texto_usuario):
        return True
    else:
        return False
        
#--------------1-----------------------
def listar_pokemones(lista:list,cantidad:int)->list:
    lista_salida = []
    if len(lista)>0 and cantidad <= len(lista):
        lista_salida = lista[-cantidad:]
        return lista_salida
    
#--------------------4-----------------------------
def calcular_promedio(lista: list, key:str)-> int:
    acumualdor = 0
    suma_key = 0
 
    for elemento in lista:
        acumualdor += 1
        suma_key += len(elemento[key])
    promedio = suma_key / acumualdor
        
    print("El promedio es: {0}".format(promedio))
    
    return int(promedio)

def calcular_mayor_menor_promedio(lista:list,dato:str,tipo:str,promedio:float):
    lista_mayor_menor = []
    for elemento in lista:
        if tipo == "mayor" and promedio < len(elemento[dato]):
            lista_mayor_menor.append(elemento)
        elif tipo == "menor" and promedio >= len(elemento[dato]):
            lista_mayor_menor.append(elemento)
        
    return lista_mayor_menor

#---------------5----------------------
def buscar(lista:list,patron:str):
    lista_tipo = []
    for elemento in lista:
        for tipo in elemento["tipo"]:
            match = re.search(patron,tipo,re.IGNORECASE)
            if match :
                titulo = tipo
                palabra = "\033[0;31m"+ match.group(0)+ "\033[0;m"
                titulo = titulo.replace(match.group(0),palabra)
                
                tipo = ", ".join(elemento["tipo"])
                evo = ", ".join(elemento["evoluciones"])
                fort = ", ".join(elemento["fortaleza"])
                deb = ", ".join(elemento["debilidad"]) 
                
                print("ID: {0} |Nombre: {1} |Tipo: {2} |Evoluciones: {3} |Poder: {4} |Fortaleza: {5} |Debilidad: {6}"
                .format(elemento["id"],elemento["nombre"],titulo,evo,elemento["poder"],fort,deb))
                
                #lista_tipo.append(elemento)
    
    #mostrar(lista_tipo)      
          
            