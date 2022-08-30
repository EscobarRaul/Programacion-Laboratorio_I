#La división de alimentos está trabajando en un pequeño software para cargar las
#compras de ingredientes para la cocina de Industrias Wayne.
#Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
#preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
#1. PESO: (entre 10 y 100 kilos)
#2. PRECIO POR KILO: (mayor a 0 [cero]).
#3. TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
#Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de
#descuento sobre el precio bruto. o si compro más de 300 kilos en total, tenes 25% de
#descuento sobre el precio bruto.
#A. El importe total a pagar, BRUTO sin descuento.
#B. El importe total a pagar con descuento (Solo si corresponde).
#C. Informar el tipo de alimento más caro.
#D. El promedio de precio por kilo en total.


respuesta = "s"
acumulador_kilos = 0
acumulador_precio_bruto = 0

acumulador_animal = 0
acumulador_precio_animal = 0
acumulador_vegetal = 0
acumulador_precio_vegetal = 0
acumulador_mezcla = 0
acumulador_precio_mezcla = 0

contador_precio = 0

while (respuesta == "s"):

    peso = input("Ingrese el peso: (entre 10 y 100 kilos) \n")
    peso = float(peso)
    while(peso <= 10 or peso >= 100):
        peso = input("ERROR!! ReIngrese el peso: (entre 10 y 100 kilos)\n")
        peso = float(peso)

    precio = input("Ingrese el precio: \n")
    precio = float(precio)
    while(precio < 0):
        precio = input("ERROR! ReIngrese el precio: (mayor a 0) \n")
        precio = float(precio)

    tipo = input("Ingese el tipo: (vegetal, animal, mezcla)\n")
    while(tipo != "vegetal" and tipo != "animal" and tipo != "mezcla"):
        tipo = input("ERROR!! ReIngese el tipo: (vegetal, animal, mezcla)\n")

    contador_precio += 1

    #A)
    precio_bruto = precio * peso
    acumulador_kilos += peso
    acumulador_precio_bruto += precio_bruto

    #C)
    if (tipo == "animal"): 
      acumulador_animal += peso
      acumulador_precio_animal += precio_bruto
    elif (tipo == "vegetal"):
        acumulador_vegetal += peso
        acumulador_precio_vegetal += precio_bruto
    else: 
        acumulador_mezcla += peso
        acumulador_precio_mezcla += precio_bruto
    
    respuesta=input("Desea continuar? s/n ")
    

#B
if (acumulador_kilos >= 300): 
    descuento = acumulador_kilos * 25 / 100
    precio_descuento = acumulador_kilos - descuento
  
elif (acumulador_kilos >= 100 and acumulador_kilos <= 300): 
      descuento = acumulador_kilos * 15 / 100
      precio_descuento = acumulador_kilos - descuento
    
else :
      precio_descuento = acumulador_kilos
    
  #alert("El descuento es: " + precioDescuento)

# C 
if (acumulador_precio_vegetal > acumulador_precio_animal and acumulador_precio_vegetal > acumulador_precio_mezcla):
    tipo_mas_caro = "vegetal"
elif (acumulador_precio_animal > acumulador_precio_mezcla):
      tipo_mas_caro = "animal"
else:
      tipo_mas_caro = "mezcla"

# D 
promedio = acumulador_precio_bruto / contador_precio

print("El importe bruto es: "+ str(precio_bruto) )
print("El importe total a pagar con descuento es: "+ str(precio_descuento))
print("El tipo de alimento mas caro es: "+ tipo_mas_caro)
print("El promedio de precio por kilo es: "+ str(promedio))
