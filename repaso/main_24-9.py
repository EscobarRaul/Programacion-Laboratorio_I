"""
1- Listar TOP n videos
2- Ordenar videos por duración (UP/DOWN)
3- Ordenar videos por cantidad de views (UP/DOWN)
4- Buscar videos por titulo
5- Exportar lista de videos a CVS
6- Salir

"""
# from func import cargar_json
# from func import *

import func


def paulina_app():
    lista_videos = func.cargar_json("Ruta relativa")
    print(lista_videos)
    while(True):
        print("1- Listar TOP n videos\n"
        "2- Ordenar videos por duración (UP/DOWN)\n"
        "3- Ordenar videos por cantidad de views (UP/DOWN)\n"
        "4- Buscar videos por titulo\n"
        "5- Exportar lista de videos a CVS\n"
        "6- Salir\n")
        respuesta = input()

        if(respuesta == "1"):
            top = int(input("\nCantidad de elementos a mostrar?: "))
            #VALIDAR QUE TOP SEA UN INT 
            func.mostrar(lista_videos[:top])
        elif(respuesta == "2"):
            func.mostrar(func.nahuel_sort(lista_videos,"length","down"))
        elif(respuesta == "3"):
            func.mostrar(func.nahuel_sort(lista_videos,"views","up"))
        elif(respuesta == "4"):
            patron = input("Buscar: ")
            func.buscar(lista_videos,patron)
        elif(respuesta == "5"):
            func.buscarexportar_csv(lista_videos,"ruta relativa")
        elif(respuesta == "6"):
            break