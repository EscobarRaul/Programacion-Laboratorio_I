
lista = [1,2,5,0,3,7,9,4]

#----------------Algoritmo nahuel---------------
def buscar_minimo(lista_a_buscar:list)->int:
    minimo = 0
    for i in range(len(lista_a_buscar)):
        if(lista_a_buscar[i] < lista_a_buscar[minimo]):
            minimo = i
    return minimo

def nahuel_sort(lista_a_ordenar)->list:
    lista_recibida = lista_a_ordenar[:]# Shallow copy ** copia de la lista original
    
    pass


#----------------Algoritmo ivan---------------
def ivan_sort(lista_a_ordenar:list)->list:
    lista_recibida = lista_a_ordenar[:] # Shallow copy ** copia de la lista original
    flag_swap = True

    limite = 1
    
    while(flag_swap == True):
        flag_swap = False
        for i in range(len(lista_recibida) - limite):
            if lista_recibida[i] > lista_recibida[i+1]:
                #buffer = lista_recibida[i]
                lista_recibida[i],lista_recibida[i+1] = lista_recibida[i+1],lista_recibida[i] # SWAP en python
                #lista_recibida[i+1] = buffer
                flag_swap = True
        
        limite +=1
    return lista_recibida


#---------------------- Qsort ------------------------------
def qsort(lista_a_ordenar:list)->list:
    lista_recibida = lista_a_ordenar[:] # Shallow copy ** copia de la lista original
    lista_de = []
    lista_iz = []
    
    if len(lista_a_ordenar) <= 1:
        
        return lista_a_ordenar
    
    else:
        pivot = lista_recibida[0]# Elijo un pivot
        for elemento in lista_recibida[1:]: #no tomo el 0 porque es mi pivot  
            if(elemento > pivot):
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    
    lista_iz = qsort(lista_iz)
    lista_iz.append(pivot)
    
    lista_de = qsort(lista_de)

    return lista_iz + lista_de


lista_resultado = qsort(lista)
print(lista_resultado)

# lista_resultado = ivan_sort(lista)
# print(lista_resultado)


#cambiar el valor de a con b
# a = 11
# b = 12
# c = a
# a = b 
# b = c

#python
#a,b = b,a