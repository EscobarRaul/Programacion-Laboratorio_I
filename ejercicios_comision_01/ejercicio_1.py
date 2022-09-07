# 1- Crear un diccionario llamado mi_dic que almacene la siguiente información de una persona:
# nombre: Karen
# apellido: Jurgens
# edad: 35
# ocupacion: Periodista

# 2- ​​Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
# nombre: Karen
# apellido: Jurgens
# edad: 36
# ocupacion: Editora
# pais: Colombia

# 3- Crear una lista que contenga distintos tipos de datos. Por ejemplo: [1,3,”Nueve”].
# 	a) Crea un algoritmo que imprima solo los elementos de la lista que son un número. 
# 	b) Crear una nueva lista con los elementos que no son un número:

mi_dic = {"nombre": "Juan", "apellido": "Jurgens", "edad": 35 , "ocupacion": "Periodista"}
print(mi_dic["edad"])
#mi_dic = {"nombre": "Juan", "apellido": "Jurgens", "edad": 36 , "ocupacion": "Editora", "pais": "Colombia"}
mi_dic["edad"]=36
mi_dic["ocupacion"]= "Editora"
mi_dic.append = {"pais":"Colombia"}
print(mi_dic)

lista_datos = [1 , 3, "Nueve"]

