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

#-----------A)NOMBRES MASCULINOS-------------
def imprimir_nombre_masculino():
    for heroe in lista_personajes :
        if heroe["genero"] == "M" :
            print("Nombres heroes masculinos: {0}".format(heroe["nombre"]))

#-----------B) NOMBRES FEMENINOS-------------
def imprimir_nombre_femenino():
    for heroe in lista_personajes :
        if heroe["genero"] == "F" :
            print("Nombres heroes Femeninos: {0}".format(heroe["nombre"]))

#------------C) HEROE MAS ALTO MASCULINO-----------
def calcular_heroe_mas_alto_masculino():
    def buscar_primer_masculino():
        heroe_masculino = {}
        for heroe in lista_personajes:
            if heroe["genero"] == "M":
                heroe_masculino = heroe
                break
        return heroe_masculino

    heroe_mas_alto = buscar_primer_masculino()
    heroe_mas_alto["altura"] = float(heroe_mas_alto["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["genero"] == "M" and heroe["altura"] > heroe_mas_alto["altura"]):
            heroe_mas_alto = heroe

    print("Nombre: {0} | altura : {1} mts. ".format(heroe_mas_alto["nombre"], heroe_mas_alto["altura"]))

#-----------------D)HEROE MAS ALTO FEMENINO----------------
def calcular_heroe_mas_alto_femenino():
    def buscar_primer_femenino():
        heroe_femenino = {}
        for heroe in lista_personajes:
            if heroe["genero"] == "F":
                heroe_femenino = heroe
                break
        return heroe_femenino

    heroe_mas_alto = buscar_primer_femenino()
    heroe_mas_alto["altura"] = float(heroe_mas_alto["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["genero"] == "F" and heroe["altura"] > heroe_mas_alto["altura"]):
            heroe_mas_alto = heroe

    print("Nombre: {0} | altura: {1} mts. ".format(heroe_mas_alto["nombre"], heroe_mas_alto["altura"]))

#--------------E) HEROE MAS BAJO MASCULINO----------------
def calcular_heroe_mas_bajo_masculino():
    heroe_mas_bajo = buscar_primer_masculino()
    heroe_mas_bajo["altura"] = float(heroe_mas_bajo["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["genero"] == "M" and heroe["altura"] < heroe_mas_bajo["altura"]):
            heroe_mas_bajo = heroe

    print("Nombre: {0} | altura : {1} mts. ".format(heroe_mas_bajo["nombre"], heroe_mas_bajo["altura"]))

#--------------F) HEROE MAS BAJO FEMENINO------------------
def calcular_heroe_mas_bajo_femenino():
    heroe_mas_bajo = buscar_primer_femenino()
    heroe_mas_bajo["altura"] = float(heroe_mas_bajo["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["genero"] == "F" and heroe["altura"] < heroe_mas_bajo["altura"]):
            heroe_mas_bajo = heroe

    print("Nombre: {0} | altura: {1} mts. ".format(heroe_mas_bajo["nombre"], heroe_mas_bajo["altura"]))

#--------------G)ALTURA PROMEDIO MASCULINO-----------------
def calcular_promedio_altura_masculino():
    acumulador_altura_masculino = 0
    contador_altura_masculino = 0
    for heroe in lista_personajes:
        if heroe["genero"] == "M":
            heroe["altura"] = float(heroe["altura"])
            acumulador_altura_masculino += heroe["altura"]
            contador_altura_masculino += 1

    print("Promedio de altura M: {0:.2f} cm.".format(acumulador_altura_masculino/contador_altura_masculino))

#-------------H) ALTURA PROMEDIO FEMENINO -------------------
def calcular_promedio_altura_femenino():
    acumulador_altura_femenino = 0
    contador_altura_femenino = 0
    for heroe in lista_personajes:
        if heroe["genero"] == "F":
            heroe["altura"] = float(heroe["altura"])
            acumulador_altura_femenino += heroe["altura"]
            contador_altura_femenino += 1

    print("Promedio de altura F: {0:.2f} cm.".format(acumulador_altura_femenino/contador_altura_femenino))


#------------J) CANTIDAD DE TIPOS DE COLOR DE OJOS ---------------
def cantidad_tipos_color_ojos():
    #{color ojos : color , contador : 1}
    lista_color_ojos = [{"color": lista_personajes[0]["color_ojos"],"cantidad":0}]
    for heroe in lista_personajes:
        dic_color_ojos = {}
        flag = False
        for ojos in lista_color_ojos:
            if(heroe["color_ojos"] == ojos["color"]):
                ojos["cantidad"] += 1
                flag = True

        if (flag == False):
            dic_color_ojos = {"color":heroe["color_ojos"], "cantidad":1}
            lista_color_ojos.append(dic_color_ojos)

    print(lista_color_ojos)

#------------K) CANTIDAD DE TIPOS DE COLOR DE PELO ------------------
def cantidad_tipos_color_pelo():
    lista_color_pelo = [{"color": lista_personajes[0]["color_pelo"],"cantidad":0}]
    for heroe in lista_personajes:
        dic_color_pelo = {}
        flag = False
        for pelo in lista_color_pelo:
            if(heroe["color_pelo"] == pelo["color"]):
                pelo["cantidad"] += 1
                flag = True

        if (flag == False):
            dic_color_pelo = {"color":heroe["color_pelo"], "cantidad":1}
            lista_color_pelo.append(dic_color_pelo)

    print(lista_color_pelo)

#--------------L) CANTIDAD 



#------------------------MENU-------------------------   
while True:
  respuesta = input("1) Nombre de heroes masculinos:\n2)Nombre de heroes femeninos:\n3)Heroe masculino mas alto:\n"
                    "4)Heroe femenino mas alto:\n5)Heroe masculino mas bajo:\n6)Heroe femenino mas bajo:\n"
                    "7)Promedio de altura masculino:\n8) Promedio de altura femenino:\n9) Cantidad de tipos de color de ojos:\n"
                    "10)Cantidad de tipos de color de pelo:\n")
  if(respuesta == "1"):
    imprimir_nombre_masculino()
  elif(respuesta == "2"):
    imprimir_nombre_femenino()
  elif(respuesta == "3"):
    calcular_heroe_mas_alto_masculino()
  elif(respuesta == "4"):
    calcular_heroe_mas_alto_femenino()
  elif(respuesta == "5"):
    calcular_heroe_mas_bajo_masculino()
  elif(respuesta == "6"):
    calcular_heroe_mas_bajo_femenino()
  elif(respuesta == "7"):
    calcular_promedio_altura_masculino()
  elif(respuesta == "8"):
    calcular_promedio_altura_femenino()
  elif(respuesta == "9"):
    cantidad_tipos_color_ojos()
  elif(respuesta == "10"):
    cantidad_tipos_color_pelo()
  elif(respuesta == "11"):
      break