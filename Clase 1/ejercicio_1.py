#La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.

# Se debe informar lo siguiente:
#1)Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#2)Del ítem con más unidades, el fabricante.
#3)Cuántas unidades de jabones hay en total.

#a) declarar variables y realizar las iteraciones con el usuario
#b) analizar la logica
#c) mostrar el resultado

flag_precio = True

acumulador_unidades_jabon = 0
acumulador_unidades_barbijo = 0

for i in range(6):
    
    tipo = input("Ingrese el tipo de producto: (barbijo / jabon / alcohol)\n")  
    while (tipo != "jabon" and tipo != "barbijo" and tipo != "alcohol"):
        tipo = input("ERROR! Ingrese el tipo de producto: (barbijo / jabon / alcohol)\n")

    precio = input("Ingrese el precio: \n")
    precio = float(precio)
    while(precio < 100 or precio > 300 ):
        precio = input("ERROR! Ingrese el precio: \n")
        precio = float(precio)
        
    cantidad_unidades = input("Ingrese la cantidad de unidades: (entre 0 y 1000) \n")
    cantidad_unidades = int(cantidad_unidades)
    while(cantidad_unidades < 0 or cantidad_unidades > 1000):
        cantidad_unidades = input("ERROR! Ingrese la cantidad de unidades: (entre 0 y 1000) \n")
        cantidad_unidades = int(cantidad_unidades)
        
    marca = input("Ingrese la marca: \n")

    fabricante = input("Ingrese el fabricante: \n")
    
    # 1)
    if (tipo == "barbijo"):
        acumulador_unidades_barbijo += cantidad_unidades
        if(flag_precio == True):
            barbijo_mas_caro = precio
            unidades_mas_caro = cantidad_unidades
            fabricante_mas_caro = fabricante
            flag_precio = False
        elif (barbijo_mas_caro < precio):
            barbijo_mas_caro = precio
            unidades_mas_caro = cantidad_unidades
            fabricante_mas_caro = fabricante
            
    elif(tipo =="alcohol"):
        acumulador_unidades_alcohol += cantidad_unidades
        
     #3
    else:
        acumulador_unidades_jabon += cantidad_unidades
           
    #2 MAAAAL
    """
    if(flag_unidades == True):
        tipo_mas_unidades = tipo
        fabricante_mas_unidades = fabricante
        flag_unidades = False
    elif(tipo_mas_unidades < tipo):
        tipo_mas_unidades = tipo
        fabricante_mas_unidades = fabricante
    """
   # 2 BIEN! 
if(acumulador_unidades_barbijo > acumulador_unidades_alcohol and acumulador_unidades_barbijo > acumulador_unidades_jabon):
    tipo_mas_unidades = "barbijo"
    fabricante_mas_unidades = fabricante
elif(acumulador_unidades_alcohol > acumulador_unidades_jabon):
    tipo_mas_unidades = "alcohol"
    fabricante_mas_unidades = fabricante
else:
    tipo_mas_unidades = "jabon"
    fabricante_mas_unidades = fabricante
        

print("El mas caro de los barbijos tiene una cantidad de: "+ str(barbijo_mas_caro) +" unidades y el fabricante es : " + fabricante_mas_caro)
print("El item con mas unidades es: "+ tipo_mas_unidades +" y el fabricante es: " + fabricante_mas_unidades)
print("La cantidad de jabones es: " + str(acumulador_jabon))


    
