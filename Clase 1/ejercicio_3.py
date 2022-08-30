"""
La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas y héroes, para para tener un control de las condiciones de heroes existentes, nos solicitan:
Nombre de Heroína/Héroe
EDAD (mayores a 18 años)
Sexo ("m", "f" o "nb")
Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
A)Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
B)El sexo y nombre de Heroe | Heroína de mayor edad.
C)La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
D)El promedio de edad entre Heroinas.
E)El promedio de edad entre Heroes de fuerza.
"""

respuesta = "s"
flag_joven = True
flag_mas_edad = True 

contador_heroinas = 0
acumulador_edad_heroinas = 0
contador_edad_heroina = 0

acumulador_edad_heroes = 0
contador_edad_heroes = 0

while (respuesta == "s"):

    nombre = input ("Ingrese el nombre de Heroe/Heroina : \n" )

    while(True):
        edad = input("Ingrese la edad : \n")
        edad = int(edad)
        if edad >= 18:
            break
    
    while(True):
        sexo = input("Ingrese el sexo : (masculino/femenino/no binario)\n")
        if sexo == "masculino" or sexo == "femenino" or sexo == "no binario":
            break

    while(True):
        habilidad = input("Ingrese la habilidad : (fuerza , magia , inteligencia)\n")
        if habilidad == "fuerza" or habilidad == "magia" or habilidad == "inteligencia":
            break
    
    #A) Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
    if habilidad == "fuerza":
        if (flag_joven == True):
            edad_mas_joven = edad
            nombre_mas_joven = nombre
            flag_joven = False
        elif (edad_mas_joven > edad ):
            edad_mas_joven = edad
            nombre_mas_joven = nombre

    #B) El sexo y nombre de Heroe | Heroína de mayor edad.
    if (flag_mas_edad == True):
        edad_mas_viejo = edad
        sexo_mas_viejo = sexo
        nombre_mas_viejo = nombre
        flag_mas_edad = False
    elif (edad_mas_viejo < edad):
        edad_mas_viejo = edad
        sexo_mas_viejo = sexo
        nombre_mas_viejo = nombre

    #C)La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
    if sexo == "femenino":
        acumulador_edad_heroinas += edad
        contador_edad_heroina += 1
        if (habilidad == "fuerza" or habilidad == "magia"):
            contador_heroinas += 1
    
    #E)El promedio de edad entre Heroes de fuerza.
    if (sexo == "masculino" and habilidad == "fuerza") :
        acumulador_edad_heroes += edad
        contador_edad_heroes += 1

    respuesta = input("Desea continuar? s/n ")

#D)El promedio de edad entre Heroinas.
promedio_edad = acumulador_edad_heroinas / contador_edad_heroina
#E)El promedio de edad entre Heroes de fuerza.
promedio_edad_heroes = acumulador_edad_heroes / contador_edad_heroes

print ("El nombre de Héroe | Heroína de fuerza más joven es: "+ nombre_mas_joven)
print ("El sexo y nombre de Heroe | Heroína de mayor edad es: " + sexo_mas_viejo +", "+nombre_mas_viejo + " con "+ str(edad_mas_viejo)+" años")
print ("La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia' es: "+ str(contador_heroinas)) 
print("El promedio de edad entre Heroinas es: "+ str(promedio_edad)+" años.")
print("El promedio de edad entre Heroes de fuerza es : "+str(promedio_edad_heroes)+ " años.")
