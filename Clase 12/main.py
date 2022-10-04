'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones
import re

def starwars_app():
    lista_personajes = funciones.cargar_json("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 12/data.json")
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        while True:
            respuesta = input("Ingrese una opción:\n")
            if funciones.validar_dato(respuesta,"^[1-6]{1}$"):
                break
            else:
                print("Error ingrese un numero de las opciones")
        if(respuesta=="1"):
            #orden = input("De que manera desea ordenar la lista:\n Asc o Desc").lower()
            lista_ordenada = funciones.ordenar(lista_personajes, "height")
            funciones.mostrar(lista_ordenada)
            #print("1 - Listar los personajes ordenados por altura\n")
        elif(respuesta=="2"):
            genero = input("Ingrese el genero del mas alto: \n female o male")
            personaje_alto_genero = funciones.mostrar_personaje_mas_alto_genero(lista_personajes, genero)
            funciones.mostrar(personaje_alto_genero)
            #print("2 - Mostrar el personaje mas alto de cada genero\n")
        elif(respuesta=="3"):
            lista_ordenada = funciones.ordenar(lista_personajes, "mass")
            funciones.mostrar(lista_ordenada)
            #print("3 - Ordenar los personajes por peso\n")
        elif(respuesta=="4"):
            personaje = ""
            while not re.match("Luke Skywalker|C-3PO|R2-D2|Darth Vader|Leia Organa|Owen Lars|Beru Whitesun lars|R5-D4|Biggs Darklighter|Obi-Wan Kenobi", personaje):
                buscador = input("ingrese el nombre del personaje a buscar:\n"
                                 "ej: Luke Skywalker, C-3PO, R2-D2, Darth Vader, Leia Organa, Owen Lars, Beru Whitesun lars, R5-D4, Biggs Darklighter, Obi-Wan Kenobi ")
                funciones.buscar_personajes(lista_personajes,buscador)
            #print("4 - Armar un buscador de personajes\n")
        elif(respuesta=="5"):
            funciones.exportar_csv(lista_personajes,"C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 12/archivo.csv" )
            print("Se genero un archivo CSV.")
            #print("5 - Exportar lista personajes a CSV\n")
        elif(respuesta=="6"):
            print("Fin del Programa")
            break


starwars_app()

