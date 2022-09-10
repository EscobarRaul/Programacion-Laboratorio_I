from data_stark import lista_personajes

"""
 {
    "nombre": "Gamora",
    "identidad": "Gamora Zen Whoberi Ben Titan",
    "empresa": "Marvel Comics",
    "altura": "183.65000000000001",
    "peso": "77.769999999999996",
    "genero": "F",
    "color_ojos": "Yellow",
    "color_pelo": "Black",
    "fuerza": "85",
    "inteligencia": "good",
    "k_entera": 1,
    "k_float": 1.5,
    "k_lista": ["pepe argento"],
    "k_dict":{"edad":32}
  }
"""

#heroe_ejemplo = lista_personajes[7]

#"nombre": "pepe"
dict_numeros = {
    "numeros" : [1,3,12,24,45,50]  
}

lista_valores = dict_numeros["numeros"]



def calcular_numeros_par_impar(lista_numeros:list, resto: int)-> list[int]:
    """
    calcula los numeros pares de una lista pasada por parametros
    y los guardara en una lista aux que solo contenga numeros pares
    
    Parametros:
    lista_numeros: la lista original a iterar
    resto: El valor que voy a evaluar para que me devuelva numeros pares o impares
    
    Retorna: La lista de numeros pares si los hay. lista vacia caso contrario
    """
    numeros_filtrados = []
    for numero in lista_numeros :
        # numeros pares
        if numero % 2 == resto:
            #lo guardo en una lista auxiliar
            numeros_filtrados.append(numero)
    
    return numeros_filtrados
                       
#######################################
#llamo la funcion
#Obtengo mi lista de pares
lista_pares = calcular_numeros_par_impar(lista_valores, 0) 
lista_impares = calcular_numeros_par_impar(lista_valores, 1) 

dict_numeros["numeros_pares"] = lista_pares
dict_numeros["numeros_impares"] = lista_impares
# tenemos la lista con numeros pares = lista_pares
#dict_numeros["numeros_pares"] = lista_pares

print(dict_numeros)


    
    
# nombres = [2,25,7]

# for num in numeros:
#     #Vemos que tiene el diccionario
#     numero_anterior = dict_numeros["numeros"]
#     dict_numeros["numeros"] += num #traigo los elementos de la lista
#     print(numero_anterior)
    