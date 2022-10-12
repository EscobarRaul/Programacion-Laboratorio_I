persona_1 = {
    "nombre": "Maximo",
    "apellido": "Cozzetti",
    "domicilio": {
        "calle": "Av. Mitre",
        "altura": 750,
        "localidad": "Avellaneda",
        "barrio": "Avellaneda Centro",
        "cod_postal" : "C1870"
    },    
    "telefonos": [
        {
            "etiqueta": "fijo",
            "cod_pais": "+54",
            "cod_area": "11",
            "numero": "4201-4133"
        },
        {
            "etiqueta": "movil",
            "cod_pais": "+54",
            "cod_area": "11",
            "nro": "4353-0220"
        }
    ],
    
    "identificacion": {
        "tipo": "dni",
        "nro": "30.505.003"
    }
}

from copy import deepcopy

# Punto 1: Modificar la calle y altura de 'persona_1' por Ramón Franco 5050. 

persona_1["domicilio"].update({"calle":"Ramón Franco","altura":5050})

#print(persona_1)

# Punto 2: Verificar si existe un numero de telefono con la etiqueta 'trabajo'. Si no existe, entonces crearlo con el valor +54 11 4201-4133. Caso contrario actualizarlo
#persona_1["telefonos"].append({"etiqueta": "trabajo","cod_pais": "+54","cod_area": "11","numero": "4201-4133"})
if persona_1["telefonos"] != "trabajo":
    persona_1["telefonos"].append({"etiqueta": "trabajo","cod_pais": "+54","cod_area": "11","numero": "4201-4133"})
    # print(persona_1)
else: 
    print("Ya existe esta etiqueta")
    

#------------------ Punto 3: ----------------------------
# imprimir los datos completos de persona_1 recorriendo todas sus claves y valores

#print(persona_1.items())
# for dato in persona_1:
#     print("{0} - {1}".format(dato,persona_1[dato]))

#for key,value in persona_1.items():
    
    
# ------------------Punto 4:------------------------------ 
#   Obtener el id de 'persona_1' y de 'persona_2'. 
#   Comprarlos, si son iguales imprirmir: 
#       "'ID de persona_1 es: id_persona_1 y el ID de persona_2 es: id_persona_2 entonces son el mismo diccionario' caso contrario imprimir "No son el mismo diccionario"
#   Modificar el nombre y apellido de persona_1 por Emilio Ravenna
#   Imprimir persona_1 y persona_2 y analizar los resultados
"""
persona_2 = persona_1

id_persona_1 = id(persona_1)
id_persona_2 = id(persona_2)

if id_persona_1 == id_persona_2:
    print("ID de persona_1 es: {0} y el ID de persona_2 es: {1} entonces son el mismo diccionario.".format(id_persona_1,id_persona_2))
else:
    print("No son el mismo diccionario.")

persona_1.update({"nombre":"Emilio", "apellido":"Ravenna"})
    
#print("Persona 1 \n{0}\n\nPersona 2 \n{1}".format(persona_1,persona_2))
"""    
# --------------------Punto 5:-------------------- 
#   Crear persona_3 a partir de una copia superficial de persona_1
#   Modificar nombre y apellido a persona_3 por Gabriel Medina
#   Modificar el nro de documento por 28.307.401
#   Imprimir persana_1 y persona_3 y analizar los resultados

persona_3 = persona_1.copy()

persona_3.update({"nombre":"Gabriel","apellido":"Medina"})
persona_3["identificacion"].update({"nro":"28.307.401"})

# print("Persona 1 \n{0}\n\nPersona 3 \n{1}".format(persona_1,persona_3))

# --------------------Punto 6:--------------------- 
#   Crear persona_4 a partir de una copia profunda de persona_1
#   Modificar el nombre y apellido por Mario Santos
#   Modificar el nro de documento por: 29.407.901
#   Imprimir persana_1 y persona_4 y analizar los resultados

persona_4 = deepcopy(persona_1)

persona_4.update({"nombre":"Mario","apellido":"Santos"})
persona_4["identificacion"].update({"nro":"29.407.901"})

#print("Persona 1 \n{0}\n\nPersona 4 \n{1}".format(persona_1,persona_4))