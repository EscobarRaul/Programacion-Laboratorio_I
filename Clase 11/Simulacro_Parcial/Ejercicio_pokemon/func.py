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

            
        