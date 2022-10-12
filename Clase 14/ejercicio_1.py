lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el 
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'

consulta = input("Ingrese producto: \n")
cantidad = int(input("Ingrese la cantidad: \n"))
def consultar_producto(consulta:str,cantidad:int):
    while True:        
        if lista_precios.get(consulta):
            precio_total = lista_precios[consulta]["precio"] * cantidad
            print("Precio: {0} Stock: {1} Precio Total: {2}".format(lista_precios[consulta]["precio"],lista_precios[consulta]["stock"], precio_total))
        else:
            print("el articulo no se encuentra en la lista")
            
        return consulta



# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)

# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios

nueva_fruta = input("Ingrese una nueva fruta: ")
nuevo_precio = int(input("Ingrese el precio de la nueva fruta: "))
nueva_unidad = input("Ingrese la unidad de medida de la nueva fruta: ")
nuevo_stock = int(input("Ingrese el stock de la nueva fruta: "))

dic_fruta = {nueva_fruta:{"precio":nuevo_precio, "unidad_medida":nueva_unidad, "stock":nuevo_stock}}

lista_precios.update(dic_fruta)

print(lista_precios)

# Punto 4: imprimir el listado de frutas (solo su nombre)

print(list(lista_precios.keys()))

# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'

nombre_fruta = input("Ingrese la fruta que desea eliminar: ")
if lista_precios.get(nombre_fruta):
    lista_precios.pop(nombre_fruta)
    print(lista_precios)
else:
    print("el articulo no se encuentra en la lista")

