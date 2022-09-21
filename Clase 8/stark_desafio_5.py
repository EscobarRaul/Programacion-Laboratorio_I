import json
import re

def imprimir_dato(dato:str):
    """
    Recibe por parámetro un string el cual se imprime por consola. 
    La función no tendrá retorno.
    """
    print(dato)
#---------------------1.1--------------------------
def imprimir_menu_desafio_5():
    imprimir_dato(("\n-------------MENU--------------\n"
                    "A) Nombre de heroes masculinos:\n"
                    "B) Nombre de heroes femeninos:\n"
                    "C) Heroe masculino mas alto:\n"
                    "D) Heroe femenino mas alto:\n"
                    "E) Heroe masculino mas bajo:\n"
                    "F) Heroe femenino mas bajo:\n"
                    "G) Promedio de altura masculino:\n"
                    "H) Promedio de altura femenino:\n"
                    "J) Cantidad de tipos de color de ojos:\n"
                    "K) Cantidad de tipos de color de pelo:\n"
                    "L) Cantidad de tipos de inteligencia:\n"
                    "M) Heroes segun su color de ojos:\n"
                    "N) Heroes segun su color de pelo:\n"
                    "O) Heroes segun su tipo de inteligencia:\n"
                    "Z) Salir.\n"))


#imprimir_menu_desafio_5()

def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    