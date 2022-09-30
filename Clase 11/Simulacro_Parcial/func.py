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

def validar_dato_ingresado(texto_usuario:str,patron:str)-> bool:
    if re.match(patron, texto_usuario):
        return True
    else:
        return False
    
#------------------1-----------------------
def mostrar(lista:list):
    lista_salida = []
    for elemento in lista:
        print("Nombre: {0} | Altura: {1} | Peso: {2} | Fuerza: {3}".format(elemento["nombre"],elemento["altura"],elemento["peso"],elemento["fuerza"]))
        lista_salida.append(elemento)   
            
    return lista_salida

#----------------------2 y 3---------------------------
def buscar_min_max(lista:list,key:str,orden:str):
    i_min_max = 0
    for i in range(len(lista)):
        if(orden == "desc" and lista[i][key] > lista[i_min_max][key]) or (orden == "asc" and lista[i][key] < lista[i_min_max][key]):
            i_min_max = i
            
    return i_min_max

def ordenar_lista(lista:list,key:str,orden:str):
    lista_ordenada = lista.copy()
    for i in range(len(lista_ordenada)):
        index_min_max = buscar_min_max(lista_ordenada[i:],key,orden)+i
        lista_ordenada[i],lista_ordenada[index_min_max] = lista_ordenada[index_min_max],lista_ordenada[i]

    return lista_ordenada

#------------------------4-----------------
def sumar_dato_heroe(lista:list,dato:str)->str:
    """
    Recibe como parámetro una lista y un string que representara
    el dato/key de los héroesque se requiere sumar.
    Retorna la suma de todos los datos segun la key pasada por parametro.
    """
    acumulador_datos = 0 
    for heroe in lista:
        if type(heroe) == dict and len(heroe) > 0:
            acumulador_datos+= heroe[dato]
    
    acumulador_datos = round(acumulador_datos, 2)
    return acumulador_datos

def dividir(dividendo:float, divisor:float)->float:
    """
    Recibe como parámetro dos números (dividendo y divisor).
    Retorna el resultado de los numeros que se pasaron por parametro.
    """
    if divisor > 0 :
        resultado = dividendo / divisor

        return resultado
    else:
        return 0

def calcular_promedio(lista:list,dato:str)->str:
    """
    Recibe como parámetro una lista y un string que representa
    el dato del héroe que se requiere calcular el promedio
    Retorna el promedio del dato pasado por parametro.
    """
    promedio = dividir(sumar_dato_heroe(lista, dato), len(lista))

    promedio = round(promedio,2)
    print("El promedio es: {0}".format(promedio))
    return promedio

def calcular_mayor_menor_promedio(lista:list,dato:str,tipo:str,promedio:float):
    lista_mayor_menor = []
    for elemento in lista:
        if tipo == "mayor" and promedio < elemento[dato]:
            lista_mayor_menor.append(elemento)
        elif tipo == "menor" and promedio > elemento[dato]:
            lista_mayor_menor.append(elemento)
        
    return lista_mayor_menor


#----------------------5------------------------
def buscar_heroe_inteligencia(lista:list,tipo:str):
    for elemento in lista:
        match = re.search(tipo,elemento["inteligencia"],re.IGNORECASE)
        if match :
            titulo = elemento["nombre"]
            # palabra = "\033[0;31m" + match.group(0) + "\033[0;m"
            # titulo = titulo.replace(match.group(0),palabra)
            print("Heroe: {0} | inteligencia: {1}".format(titulo,elemento["inteligencia"]))


#--------------6------------------
def exportar_csv(lista:list,path:str):
    with open(path,"w") as file:
        for elemento in lista:
            file.write("Nombre: {0}, Identidad: {1}, Altura: {2}, Peso: {3}, Fuerza:{4}, Inteligencia: {5}\n"
                                                        .format(elemento["nombre"],elemento["identidad"],elemento["altura"],
                                                        elemento["peso"],elemento["fuerza"],elemento["inteligencia"]))
            