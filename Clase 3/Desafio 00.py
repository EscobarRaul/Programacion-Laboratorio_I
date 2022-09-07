"""
lista_personajes =
[
 {
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 }

"""
from data_stark import lista_personajes

# ------A)-----------
# print(lista_personajes)


def imprimir_nombre_heroes():
    # -------B)---------
  for heroe in lista_personajes:
    print("Nombre: {0}".format(heroe["nombre"]))


def imprimir_nombre_altura_heroes():
    # -------C)---------
  for heroe in lista_personajes:
    heroe["altura"] = float(heroe["altura"])
    print("Nombre: {0} - Altura: {1} cm.".format(heroe["nombre"], heroe["altura"]))


def calcular_heroe_mas_alto():
    # -------D) HEROE MAS ALTO----------
  heroe_mas_alto = lista_personajes[0]
  for heroe in lista_personajes:
    heroe_float = float(heroe["altura"])
    heroe_mas_alto_float = float(heroe_mas_alto["altura"])
    if(heroe_float > heroe_mas_alto_float):
      heroe_mas_alto = heroe
  print("Nombre: {1} - Altura: {0} cm.".format(heroe_mas_alto["altura"], heroe_mas_alto["nombre"]))


def calcular_heroe_mas_bajo():
    # ---------E) HEROE MAS BAJO ----------
  heroe_mas_bajo = lista_personajes[0]
  for heroe in lista_personajes:
    heroe_float = float(heroe["altura"])
    heroe_mas_bajo_float = float(heroe_mas_bajo["altura"])
    if(heroe_float < heroe_mas_bajo_float):
      heroe_mas_bajo = heroe

  print("Nombre: {1} - Altura: {0} cm.".format(heroe_mas_bajo["altura"], heroe_mas_bajo["nombre"]))


def calcular_promedio_altura():
    # -----------F) ALTURA PROMEDIO ------------
  acumulador_altura_heroe = 0
  for heroe in lista_personajes:
    heroe_float = float(heroe["altura"])
    acumulador_altura_heroe += heroe_float

  print("Promedio de altura: {0:.2f} cm.".format(acumulador_altura_heroe/len(lista_personajes)))


def calcular_hereo_mas_menos_pesado():
    # -----------H) HEROE MAS - MENOS PESADO -----------
  heroe_mas_pesado = lista_personajes[0]
  heroe_menos_pesado = lista_personajes[0]
  for heroe in lista_personajes:
    heroe["peso"] = float(heroe["peso"])
    if (heroe["peso"] > heroe_mas_pesado["peso"]):
      heroe_mas_pesado = heroe
    if (heroe["peso"] < heroe_menos_pesado["peso"]):
      heroe_menos_pesado = heroe

  print("Heroe mas pesado: {0} kg. - Nombre: {1}\nHeroe menos pesado: {2} kg. - Nombre: {3}".format(heroe_mas_pesado["peso"], heroe_mas_pesado["nombre"], heroe_menos_pesado["peso"], heroe_menos_pesado["nombre"]))


while True:
  respuesta = input("1) Nombre de Superheroes:\n2) Altura de cada heroe:\n3) SuperHeroe mas alto:\n"
                    "4) Superheroe mas bajo:\n5) Promedio de altura de los Superheroes\n6) Superhero Mas y Menos pesado:\n7) Salir\n")
  if(respuesta == "1"):
    imprimir_nombre_heroes()
  elif(respuesta == "2"):
    imprimir_nombre_altura_heroes()
  elif(respuesta == "3"):
    calcular_heroe_mas_alto()
  elif(respuesta == "4"):
    calcular_heroe_mas_bajo()
  elif(respuesta == "5"):
    calcular_promedio_altura()
  elif(respuesta == "6"):
    calcular_hereo_mas_menos_pesado()
  elif(respuesta == "7"):
    break
