# MIT License
#
# Copyright (c) 2022 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from funciones_sw import (
    buscar_personaje_en_lista, cargar_json, continuar_consola,
    exportar_a_csv, imprimir_menu, listar_max_por_genero,
    mostrar, ordenar_lista, validar_respuesta
)


"""
Modificar el menu y funcionalidades para que cumpla con lo siguiente:

0 - Castear las claves mass y heigt a entero usando [Map] (No sera una opcion del menu).
1 - Listar los personajes ordenados por altura [sort] [opc reverse]
2 - Mostrar el personaje mas alto de cada genero [Reduce] [Lambda]
3 - Ordenar los personajes por peso [sort] [opc reverse]
4 - Armar un buscador de personajes
5 - Filtrar personajes Femeninos [Filter] [Lambda]
6 - Filtrar personajes Masculinos [Filter] [Lambda]
7 - Filtrar personajes Sin Genero [Filter] [Lambda]
>> Nota: Si la key relacionada al genero no existe, buscar en la key 'data' y 
>> 'updatear' la key faltante con el valor correspondiente al genero, para que quede igual
>> que los diccionarios anteriores.
8 - Desordenar la lista de manera random y mostrar el ultimo de la lista [Shuffle]
9 - Exportar lista personajes a CSV
10 - Salir

"""


FILE_IN = 'C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 14/starwars.json'
FILE_OUT = './Desafios_Clase/Clase_12/Clase_12.PP_Original/starwars.csv'

def starwars_app():
    lista_personajes = cargar_json(FILE_IN)
    while(True):
        imprimir_menu()
        respuesta = validar_respuesta(input('>> '), '^[0-6]{1}$')
        if(respuesta=="1"):
            key = 'height'
            lista_a_mostrar = ordenar_lista(lista_personajes, key)
            mostrar(lista_a_mostrar, key)
        elif(respuesta=="2"):
            key = 'height'
            lista_a_mostrar = listar_max_por_genero(lista_personajes, 'n/a', key)
            lista_a_mostrar += listar_max_por_genero(lista_personajes, 'female', key)
            lista_a_mostrar += listar_max_por_genero(lista_personajes, 'male', key)
            mostrar(lista_a_mostrar, key)
        elif(respuesta=="3"):
            key = 'mass'
            lista_a_mostrar = ordenar_lista(lista_personajes, key)
            mostrar(lista_a_mostrar, key)
        elif(respuesta=="4"):
            nombre_usuario = validar_respuesta(
                input("Ingrese un nombre a buscar: "), r'^[a-zA-Z]+'
            )
            buscar_personaje_en_lista(lista_personajes, nombre_usuario)
        elif(respuesta=="5"):
            exportar_a_csv(lista_a_mostrar, FILE_OUT)
        elif(respuesta=="6"):
            break
        else:
            print('Opcion incorrecta.')
        continuar_consola()

starwars_app()
