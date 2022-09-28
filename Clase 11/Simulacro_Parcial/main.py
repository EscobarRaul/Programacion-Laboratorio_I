"""
1.Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)
2.Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
3.Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
4.Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’) y listar en consola ordenados de forma ascendente.
5.Buscar y Listar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda.
6.Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]
"""

import func

def menu():
    lista_heroes = func.cargar_json("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 11/Simulacro_Parcial/data_stark (1).json")
    while(True):
        print("\n----------------MENU-----------------\n"
              "1- Listar los primeros N heroes.\n2- Ordenar y Listar héroes por altura\n"
              "3- Ordenar y Listar héroes por fuerza\n4- Calcular promedio de cualquier key numérica\n"
              "5- Buscar y Listar héroes por inteligencia\n6- Exportar a CSV la lista de héroes ordenada\n"
              "7- Salir")
        
        respuesta = input("\nIngrese la opción: \n") #func.validar_dato_ingresado("\nIngrese la opción: \n")#
        if respuesta == "1":
            top = int(input("Los primeros cuantos heroes desea mostrar?: \n"))
            if top <= len(lista_heroes):
                func.mostrar(lista_heroes[:top])
            else:
                print("Opcion no valida Reingrese su numero:")    
        elif respuesta == "2":
            orden = input("De que manera quiere ordenar ")
        elif respuesta == "3":
            pass
        elif respuesta == "4":
            pass
        elif respuesta == "5":
            pass
        elif respuesta == "6":
            pass
        elif respuesta == "7":
            break        
        
menu()
        