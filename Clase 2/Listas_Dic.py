QTY_EMPLEADOS = 3
#lista_nombres = []
#lista_apellidos = []

lista_empleados = []


for i in range(QTY_EMPLEADOS):
    dic_empleado = {}
    nombre = input("nombre: \n")
    apellido = input("apellido: \n")
    dni = input("dni: \n")
    # VALIDAR
    # lista_nombres.append(nombre)
    # lista_apellidos.append(apellido)
    dic_empleado["nombre"] = nombre
    dic_empleado["apellido"] = apellido
    dic_empleado["dni"] = dni
    lista_empleados.append(dic_empleado)

for empleado in lista_empleados:
    print(empleado["nombre"])
    



# [0] NOMBRE - APELLIDO
# [1] NOMBRE - APELLIDO

# for i in range(QTY_EMPLEADOS):
#print("{0} - {1} - {2}".format(i,lista_nombres[i],lista_apellidos[i]))

"""
lista = [1,2,3,4,5,6]

lista [3 : 5] # va de un rango al otro (del 3 al 5 "posicion")

lista.append(22) # .append agrega un numero a la lista
lista.append(23)

for i in lista: #recorro la lista
    print(i)
    
lista_temas = ["T1","T2"]
for tema in lista_temas :
    print(tema)
#T1
#T2
"""

#creo uno vacio
mi_diccionario = {}

#creo definiendo sus claves y valores
mi_diccionario_dos = {"Clave":"valor", "diccionario":heroes_info["Shazam"]["ID"],"habiliades":heroes_info["Shazam"]["Habilidades"]}

#agrego una clave y su valor a un diccionario vacio
mi_diccionario["id"] = 25

mi_diccionario_dos["pepe"] = heroes_info["Shazam"]
mi_diccionario_dos["ID"] =heroes_info["Shazam"]["ID"]
mi_diccionario_dos["Habilidades"] =heroes_info["Shazam"]["Habilidades"]