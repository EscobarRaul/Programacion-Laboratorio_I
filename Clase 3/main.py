from data import lista_bzrp
'''
[
    
    {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
    }
]


1 - Tema mas visto
2 - Tema menos visto
3 - Tema mas largo
4 - Tema mas corto
5 - Duracion promedio de temas
6 - Promedio de vistas 
7 - Salir
'''
dic_test = {"a":22, "b":"Hola", "c":3}
print(dic_test) # {'a': 22, 'b': 'Hola', 'c': 3}

print(dic_test['a']) # 22

dic_test['a']=28
print(dic_test)

dic_test['j']=4
print(dic_test) # {'a': 28, 'b': 'Hola', 'c': 3, 'j': 4}

print(dic_test.items())
print(dic_test.values())

video_mas_largo = calcula_maximo_minimo(lista, "views","maximo")
video_mas_rep = calcula_maximo_minimo(lista, "views","minimo")
#video_mas_estrellas = calcula_maximo(lista, "star") SI SE AGREGA UN NUEVA CLAVE SOLO LO CAMBIAMOS DE ACA

#---------------ENVIAR LO DE ABAJO A UNA HOJA DE CALCULO---------------------------
def calcula_maximo_minimo(lista:list,clave:str,tipo:str)-> dict :
    """
    calcula el valor maximo/minimo en funcion a la clave recibida
    de una lista de videos 
    list: tiene que ser una lista de diccionarios
    clave: tiene que representar una clave de dict que contenga un valor numerico
    tipo: solo puede ser "maximo" o "minimo"
    
    retorno: el elemento(dict) que contiene el valor maximo 
    """
    elemento_max_min = -1
    if(type(lista)== type([]) and len(lista) > 0 and type(clave)== type("")):
        elemento_max_min = lista[0] #se toma el primer dic de la lista_bzrp
        for elemento in lista:
            if (tipo == "maximo" and elemento[clave] > elemento_max_min[clave]):
                elemento_max_min = elemento
            elif (tipo == "minimo" and elemento[clave] < elemento_max_min[clave]):
                elemento_max_min = elemento
        
    return elemento_max_min
#---------------ENVIAR LO DE ARRIBA A UNA HOJA DE CALCULO-------------------------

def calcular_tema_mas_visto():
    #---------TEMA MAS VISTO----------------
    video_maximo = lista_bzrp[0]
    for video in lista_bzrp:
        if(video["views"] >  video_maximo["views"]):
            video_maximo = video

    print("Video: {1} - Vistas: {0}".format(video_maximo["views"]/1000000,video_maximo["title"]))
    #-------------------------------------------

def calcular_tema_menos_visto():
    #---------TEMA MENOS VISTO----------------
    video_minimo = lista_bzrp[0]
    for video in lista_bzrp:
        if(video["views"] <  video_minimo["views"]):
            video_minimo = video

    print("Video: {1} - Vistas: {0}".format(video_minimo["views"]/1000000,video_minimo["title"]))
    #-------------------------------------------  
def calcular_tema_mas_largo():
    #--------- TEMA MAS LARGO ----------------
    video_length_maximo = lista_bzrp[0]
    for video in lista_bzrp:
        if(video["length"] >  video_length_maximo["length"]):
            video_length_maximo = video

    print("Video: {1} - Tiempo: {0}".format(video_length_maximo["length"],video_length_maximo["title"]))
    #-------------------------------------------
def calcular_tema_mas_corto():
    #--------- TEMA MAS CORTO ----------------
    video_length_minimo = lista_bzrp[0]
    for video in lista_bzrp:
        if(video["length"] <  video_length_minimo["length"]):
            video_length_minimo = video

    print("Video: {1} - Tiempo: {0}".format(video_length_minimo["length"],video_length_minimo["title"]))
    #-------------------------------------------

def calcular_promedio_tiempo():
    # -------- PROMEDIO TIEMPO ------------
    acumulador_tiempo_videos = 0
    for tema in lista_bzrp:
        acumulador_tiempo_videos = acumulador_tiempo_videos +  tema["length"]

    print("Promedio: {2} - QTY: {0} - ACUM: {1} ".format(len(lista_bzrp),acumulador_tiempo_videos, acumulador_tiempo_videos/len(lista_bzrp)))

def calcular_promedio_vistas():
    # -------- PROMEDIO VISTAS ------------
    acumulador_vistas_videos = 0
    for tema in lista_bzrp:
        acumulador_vistas_videos +=  tema["views"]

    print("Promedio: {0:.2f} millones".format((acumulador_vistas_videos/len(lista_bzrp))/1000000))

while True:
    respuesta = input("\n1 - Tema mas visto\n2 - Tema menos visto\n3 - Tema mas largo\n4 - Tema mas corto\n5 - Duracion promedio de temas\n6 - Promedio de vistas\n7 - Salir\n\n> ")
    if(respuesta == "1"):
        calcular_tema_mas_visto()
    elif(respuesta == "2"):
       calcular_tema_menos_visto()
    elif(respuesta == "3"):
        calcular_tema_mas_largo()
    elif(respuesta == "4"):
        calcular_tema_mas_corto()
    elif(respuesta == "5"):
        calcular_promedio_tiempo()
    elif(respuesta == "6"):
        calcular_promedio_vistas()
    elif(respuesta == "7"):
        break


































