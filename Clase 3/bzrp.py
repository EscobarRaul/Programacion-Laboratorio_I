#from data import lista_bzrp #copiar y pegar toda la lista completa.

"""
[
    {
        "title": "Quevedo" || BZRP music sessions #52,
        "views": 227192970,
        "lentgh": 204,
        "img_url": "https://"
        "url": "https://"
        "date": "2022-07-06 00:00:00"
    }
]
1 - Tema mas Visto
2 - Tema menos visto
"""
def calcular_tema_mas_visto():
    #Aca iria el for del tema mas visto
    video_maximo = lista_bzrp[0] # se declara el dic de esa posicion
    for video in lista_bzrp:
        # vistas = video["views"]
        # print(vistas)
        if(video["views"] > video_maximo["views"]):
            #views_maximo = video["views"] 
            #nombre_maximo = video["title"] 
            video_maximo = video
        
print("Video: {1} - Vistas: {0}".format(video_maximo["title"], video_maximo["views"])) 
    
while True:
    respueta = input("1 - Tema mas visto\n2 - Tema menos visto") 
    if(respueta == "1"):
        calcular_tema_mas_visto()


# for tema in lista_bzrp: # cada diccionario (tema) de la lista
#     print(tema["views"])
    
#1views_maximo = lista_bzrp[0]["views"] # mi maximo es el primer elemento
#nombre_maximo = lista_bzrp[0]["title"] # se declara el nombre maximo para imprimer el maximo con su nombre
video_maximo = lista_bzrp[0] # se declara el dic de esa posicion
for video in lista_bzrp:
    # vistas = video["views"]
    # print(vistas)
    if(video["views"] > video_maximo["views"]):
        #views_maximo = video["views"] 
        #nombre_maximo = video["title"] 
        video_maximo = video
        
print("Video: {1} - Vistas: {0}".format(video_maximo["title"], video_maximo["views"]))        

#print(video_maximo["titlte"], video_maximo["views"])

#--------Menos Visto------------
video_minimo = lista_bzrp[0] # se declara el dic de esa posicion
for video in lista_bzrp:
    if(video["views"] < video_minimo["views"]):
        #views_maximo = video["views"] 
        #nombre_maximo = video["title"] 
        video_minimo = video
print("Video: {1} - Vistas: {0}".format(video_minimo["title"], video_minimo["views"]))        

#------------------------

#---------Mas largo----------------
video_length_maximo = lista_bzrp[0] # se declara el dic de esa posicion
for video in lista_bzrp:
    if(video["length"] > video_length_maximo["views"]):
        #views_maximo = video["views"] 
        #nombre_maximo = video["title"] 
        video_length_maximo = video
print("Video: {1} - Tiempo: {0}".format(video_length_maximo["title"], video_length_maximo["length"])) 
#-----------------------------------


# -------------PROMEDIO TIEMPO -----------
#cantidad_videos = 0   Se reemplaza con el len()
acumulador_tiempo_videos = 0

for tema in lista_bzrp :
    #cantidad_videos += 1 
    acumulador_tiempo_videos += tema["lenght"] # traigo de la lista el tiempo del tema


print("Promedio:{2}- QTY:{0}- ACUM:{1} ".format(len(lista_bzrp), acumulador_tiempo_videos, acumulador_tiempo_videos/len(lista_bzrp)))


#-------------PROMEDIO DE VISTAS-----------------
acumulador_tiempo_vistas = 0

for tema in lista_bzrp : 
    acumulador_tiempo_vistas += tema["views"] # traigo de la lista el tiempo del tema


print("Promedio:{0:.2f} millones".format(acumulador_tiempo_vistas/len(lista_bzrp))) #{0:.2f} pone dos decimales despues de la coma

    
# lista = [1,"f", 3, 4]
# for elemento in lista:
#     print(elemento)

# dic_tema = lista_bzrp[14] 
# print(dic_tema["url"])

# tema = lista_bzrp[14] # tema: varible para la lista de los temas
# print(tema["title"], tema ["views"]) # imprimir el titulo del tema y los views


#print(lista_bzrp[0])#el primer elemento
#print(lista_bzrp[0]["title"])#imprimo solo el titulo del primer elemento