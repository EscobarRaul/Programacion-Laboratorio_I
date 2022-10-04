"""
1-Listar los últimos N pokemones. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)

2-Ordenar y Listar pokemones por poder. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

3-Ordenar y Listar pokemones por ID. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

4-Calcular la cantidad promedio de las key tipo lista (evoluciones, fortaleza, debilidad, tipo), Preguntar qué promedio quiere calcular este esas posibles keys y filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con tener mayores o menores cantidades en la lista de dicha key según corresponda.

5-Buscar pokemones por tipo (dar e elegir los diversos tipos que un pokémon puede poseer, muchos de ellos poseen más de un tipo, con lo cual habrá que darle a elegir al usuario entre todos los tipos que existen en el json) una vez seleccionado listar en consola los que posean dicho tipo. (Usando RegEx para la búsqueda).
Ejemplo: Si el usuario elige: volador y hay un pokemon con muchos tipos, pero uno de ellos es volador, deberá listarlo. (charizard, zapdos, moltres, articuno poseen más de un tipo, pero uno de ellos es volador).

6-Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4]
"""

import re
import func

def menu():
    lista_pokemones = func.cargar_json("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 11/Simulacro_Parcial/Ejercicio_pokemon/pokedex.json")
    while True:
        print("-----------------MENU-----------------\n"
            "1- Listar los últimos N pokemones\n"
            "2- Ordenar y Listar pokemones por poder\n"
            "3- Ordenar y Listar pokemones por ID\n"
            "4- Calcular la cantidad promedio de las key tipo lista\n"
            "5- Buscar pokemones por tipo\n"
            "6- Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4]\n"
            "7- Salir\n")
        
        respuesta = input("Ingresa una opción:\n")
        
        if respuesta == "1":
            func.mostrar(lista_pokemones)
        elif respuesta == "2":
            pass
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