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
            while True:            
                cantidad = int(input("Los ultimos cuantos pokemones desea listar?\n"))
                if func.validar_dato_ingresado(cantidad,"^[0-9]{1,2}$"):
                    lista_poke = func.listar_pokemones(lista_pokemones,cantidad)
                    func.mostrar(lista_poke)
                    break
                else:
                    print("ERROR")
            
        elif respuesta == "2":
            pass
        elif respuesta == "3":
            pass
        elif respuesta == "4":
            key_a_promediar = ""
            mayor_menor = ""
            while not re.match("^(evoluciones|fortaleza|debilidad|tipo)$", key_a_promediar):
                key_a_promediar = input("Ingrese key a promediar:\n"
                                        "Evoluciones, Fortaleza, Debilidad, Tipo: ").lower()    
            promedio = func.calcular_promedio(lista_pokemones,key_a_promediar)
            while not re.match("^(mayor|menor)$", mayor_menor):
                mayor_menor = input("Desea mostrar los pokemones que sean mayor o menor al promedio? ").lower()
                lista_promediada = func.calcular_mayor_menor_promedio(lista_pokemones, key_a_promediar, mayor_menor, promedio)
                
                func.mostrar(lista_promediada)
            
        elif respuesta == "5":
            patron = ""
            while not re.match("^(veneno|hielo|fuego|electrico|agua|acero|psiquico|lucha|"
                            "fantasma|planta|volador|electrico)$", patron):
                patron = input("ingrese el tipo:\n"
                            "veneno, hielo, fuego, electrico, agua, acero, psiquico, lucha, "
                            "fantasma, planta, volador, electrico.\n").lower()
                
                func.buscar(lista_pokemones,patron)
                 
        elif respuesta == "6":
            pass
        elif respuesta == "7":
            break
    
    

menu()