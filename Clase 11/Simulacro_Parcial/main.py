"""
1.Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)
2.Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
3.Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
4.Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’) y listar en consola ordenados de forma ascendente.
5.Buscar y Listar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda.
6.Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]
"""

import func
import re

def menu():
    lista_heroes = func.cargar_json("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 11/Simulacro_Parcial/data_stark (1).json")
    lista_a_guardar = []
    while(True):
        print("\n----------------MENU-----------------\n"
              "1- Listar los primeros N heroes.\n2- Ordenar y Listar héroes por altura\n"
              "3- Ordenar y Listar héroes por fuerza\n4- Calcular promedio de cualquier key numérica\n"
              "5- Buscar y Listar héroes por inteligencia\n6- Exportar a CSV la lista de héroes ordenada\n"
              "7- Salir")
        
        while True:
            respuesta = input("\nIngrese la opción: \n") #func.validar_dato_ingresado("\nIngrese la opción: \n")#
            if func.validar_dato_ingresado(respuesta,"^[1-7]{1}$"):
                break
            else:
                print("Error ingrese un numero de las opciones.")
            
        if respuesta == "1":
            while True:
                top = input("Los primeros cuantos heroes desea mostrar?: \n")
                if func.validar_dato_ingresado(top,"^[0-9]{1,2}$"):
                    top = int(top)
                    lista_heroes = func.mostrar(lista_heroes[:top])
                    lista_a_guardar = lista_heroes.copy()
                    break
                else:
                    print("Opcion no valida Reingrese su numero:\n")    
                            
        elif respuesta == "2":
            while True:
                orden = input("De que manera quiere ordenar (asc o desc):").lower()
                if re.match("asc|desc",orden):
                    lista_ordenada = func.mostrar(func.ordenar_lista(lista_heroes,"altura",orden))
                    lista_a_guardar = lista_ordenada.copy()
                    break
                else:
                    print("Reingrese alguna de las dos opciones.\n")
            
        elif respuesta == "3":
            while True:
                orden = input("De que manera quiere ordenar (asc o desc):").lower()
                if re.match("asc|desc",orden):
                    lista_ordenada = func.mostrar(func.ordenar_lista(lista_heroes,"fuerza",orden))
                    lista_a_guardar = lista_ordenada.copy()
                    break
                else:
                    print("Reingrese alguna de las dos opciones.\n")
            
        elif respuesta == "4":
            while True:
                dato_a_promediar = input("Ingrese que desea promediar altura | peso | fuerza:\n").lower()
                if re.match("altura|peso|fuerza", dato_a_promediar):
                    promedio = func.calcular_promedio(lista_heroes,dato_a_promediar)
                    break
                else:
                    print("ERROR!")
                    
            while True:        
                mayor_menor_heroe = input("desea mostrar los heroes que sean mayor o menor al promedio:\n")
                if re.match("mayor|menor", mayor_menor_heroe):
                    lista_promediada = func.calcular_mayor_menor_promedio(lista_heroes, dato_a_promediar, mayor_menor_heroe,promedio)
                    func.mostrar(lista_promediada)
                    lista_a_guardar = lista_promediada.copy()
                    break
                else:
                    print("ERROR!")
            
        elif respuesta == "5":
            while True:
                res_inteligencia = input("Que tipo de inteligencia desea buscar: Good, Average o High:\n").lower()
                if re.match("good|average|high",res_inteligencia):
                    func.buscar_heroe_inteligencia(lista_heroes,res_inteligencia)
                    break
                else:
                    print("Reingrese alguna de las dos opciones.\n")
        elif respuesta == "6":
            if len(lista_a_guardar) != 0:
                func.exportar_csv(lista_a_guardar, "C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 11/archivo.csv")
            else:
                print("No hay una lista generada, ingrese opcion de 1-4")
        elif respuesta == "7":
            print("Fin del Programa")
            break        
        
menu()
        