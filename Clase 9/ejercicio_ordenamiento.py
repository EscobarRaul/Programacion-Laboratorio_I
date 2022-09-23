"""
METODO NAHUEL

Recibo la lista 
genero una funcion que busco el minimo y en que posicion se encuentra

genero una copia de la lista original 
genero una lista vacia
recorro la copia con un while

"""
lista = [14,5,20,10,23,15,7,16,29,21,-102,99,0]

def buscar_minimo(lista:list):
    minimo = 0
    for i in range(len(lista)):
        if(lista[i] < lista[minimo]):
            minimo = i
    return minimo

print(buscar_minimo(lista))

def ordenar_lista(lista:list):
    lista_copia = lista[:] # copia de la lista original
    lista_ordenada = []
    while(len(lista_copia) > 0):
        minimo = buscar_minimo(lista_copia)
        lista_ordenada.append(lista_copia.pop(minimo))
        
    return lista_ordenada

print(ordenar_lista(lista))
        
    