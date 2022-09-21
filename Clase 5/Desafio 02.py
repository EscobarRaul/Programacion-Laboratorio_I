from data_stark import lista_personajes

#---------------0.0----------------
def stark_normalizar_datos (lista:list)->list:
    """
    Recorre una lista y convierte al tipo de dato correcto las keys
    Valida primero que el tipo de dato no sea del tipo al cual será casteado
    lista: tiene que ser una lista de diccionarios
    retorna: los datos ya casteados a enteros o flotantes  
    """
    if len(lista_personajes) > 0:
        flag = True 
        for elemento in lista:
            if(type(elemento) != type(float())):
                elemento["altura"] = float(elemento["altura"])
                flag = False
            if(type(elemento) != type(float())):
                elemento["peso"] = float(elemento["peso"])
                flag = False
            if(type(elemento) != type(int())):
                elemento["fuerza"] = int(elemento["fuerza"])
                flag = False
        if flag == False:
            pass
            #print("Datos Normalizados")
    else: 
        print("Error: Lista de héroes vacía")


#stark_normalizar_datos(lista_personajes)
    
#-----------1.1-----------------------

def obtener_nombre(diccionario:dict)->str:
    """
    Recibe por parámetro un diccionario
    devuelve un string el cual contenga su nombre formateado
    """
    nombre_heroe = "Nombre: {0}".format(diccionario["nombre"])
    
    return nombre_heroe
     
#print(obtener_nombre(lista_personajes[0]))
   
#------------1.2---------------------
def imprimir_dato(dato:str):
    """
    Recibe por parámetro un string el cual se imprime por consola. 
    La función no tendrá retorno.
    """
    print(dato)
    
#------------1.3---------------------
def stark_imprimir_nombres_heroes(lista:list):
    """
    Recibe por parámetro la lista de héroes la cual se imprimira en la consola
    Valida que la lista no se encuentre vacia.
    """
    if type(lista) == list :
        for nombre in lista:
            imprimir_dato(obtener_nombre(nombre))   
    else:
        return -1
    
#stark_imprimir_nombres_heroes(lista_personajes)

#--------------2-----------------------
def obtener_nombre_y_dato(heroe:dict, dato:str)->str:
    """
    Recibe por parámetro un diccionario y un string como dato
    La funcion devuelve un string con el nombre y dato que se desea imprimir
    """
    nombre_dato = "{0} | {1}: {2}".format(obtener_nombre(heroe),dato,heroe[dato])
    
    return nombre_dato

# for heroe in lista_personajes:
#     imprimir_dato(obtener_nombre_y_dato(heroe,"fuerza"))
        
#---------------3-----------------------------
def stark_imprimir_nombres_alturas(lista:list)->list:
    """
    Recibe por parámetro una lista, la cual deberá iterar e imprimir sus nombres y alturas.
    Valida que la lista no se encuentre vacia.
    """
    if len(lista) > 0:
        for heroe in lista:
            imprimir_dato(obtener_nombre_y_dato(heroe, "altura"))
    
    else:
        print ("ERROR!")
        return -1
    
#stark_imprimir_nombres_alturas(lista_personajes)

#--------------------4.1------------------------
def calcular_max(lista:list,dato:str)->str:
    """
    Recibe por parámetro una lista y un string, la cual representará el dato que deberá 
    ser evaluado a efectos de determinar cuál es el máximo de la lista.
    Retorna el heroe con el dato mas alto.
    """
    stark_normalizar_datos(lista)
    heroe_max = lista[0]
    for heroe in lista:
        if heroe[dato] > heroe_max[dato]:
            heroe_max = heroe
    
    return heroe_max

#imprimir_dato(obtener_nombre_y_dato(calcular_max(lista_personajes, "altura"), "altura"))

#----------------4.2-----------------------------
def calcular_min(lista:list,dato:str)->str:
    """
    Recibe por parámetro una lista y un string, la cual representará el dato que deberá 
    ser evaluado a efectos de determinar cuál es el máximo de la lista.
    Retorna el heroe con el dato mas bajo.
    """
    stark_normalizar_datos(lista)
    heroe_min = lista[0]
    for heroe in lista:
        if heroe[dato] < heroe_min[dato]:
            heroe_min = heroe
    
    return heroe_min

#imprimir_dato(obtener_nombre_y_dato(calcular_min(lista_personajes, "altura"), "altura"))

#-----------------4.3---------------------------
def calcular_max_min_dato(lista:list,tipo:str,dato:str)->str:
    """
    Recibe por parametros 3 datos:
    lista = tiene que ser una lista de diccionarios.
    tipo = es del type string y se le pasa ya sea el minimo o maximo.
    dato = es del type string y se le pasa el dato al que se desea obtener el max o min.
    Retorna al heroe que cumpla con la condicion pedida.
    """
    if(tipo == "maximo"):
        heroe_max_min = calcular_max(lista, dato)
    elif(tipo == "minimo"):
        heroe_max_min = calcular_min(lista, dato)
    return heroe_max_min

#imprimir_dato(obtener_nombre_y_dato(calcular_max_min_dato(lista_personajes,"minimo", "peso"), "peso") )

#------------------4.4-------------------------
def stark_calcular_imprimir_heroe(lista:list,tipo:str,dato:str)->str:
    """
    Recibe por parametro:
    lista = tiene que ser una lista de diccionarios.
    tipo = es del type string y se le pasa ya sea el minimo o maximo.
    dato = es del type string y se le pasa el dato al que se desea obtener el max o min.
    Retorna al heroe y lo imprime por consola.
    """
    if len(lista) > 0:
        imprimir_dato("{0} {1}: {2}".format(tipo.capitalize(),dato,obtener_nombre_y_dato(calcular_max_min_dato(lista, tipo, dato), dato)))
    
    else:
        return -1
#stark_calcular_imprimir_heroe(lista_personajes, "minimo" , "peso")
    
#----------------5.1-------------------------
def sumar_dato_heroe(lista:list,dato:str)->str:
    """
    Recibe como parámetro una lista y un string que representara
    el dato/key de los héroesque se requiere sumar.
    Retorna la suma de todos los datos segun la key pasada por parametro.
    """
    stark_normalizar_datos(lista)
    acumulador_datos = 0 
    for heroe in lista:
        if type(heroe) == dict and len(heroe) > 0:
            acumulador_datos+= heroe[dato]
    
    acumulador_datos = round(acumulador_datos, 2)
    return acumulador_datos

#print(sumar_dato_heroe(lista_personajes, "peso"))

#----------------5.2-----------------------
def dividir(dividendo:float, divisor:float)->float:
    """
    Recibe como parámetro dos números (dividendo y divisor).
    Retorna el resultado de los numeros que se pasaron por parametro.
    """
    if divisor > 0 :
        resultado = dividendo / divisor

        return resultado
    else:
        return 0
               
#print(dividir(4, 0))

#-----------------5.3--------------------
def calcular_promedio(lista:list,dato:str)->str:
    """
    Recibe como parámetro una lista y un string que representa
    el dato del héroe que se requiere calcular el promedio
    Retorna el promedio del dato pasado por parametro.
    """
    promedio = dividir(sumar_dato_heroe(lista, dato), len(lista))

    promedio = round(promedio,2)
    return promedio

#print(calcular_promedio(lista_personajes, "altura"))

#-------------------5.4------------------
def stark_calcular_imprimir_promedio_altura(lista:list)->list:
    """
    Recibe una lista.
    Calculara y mostrara el promedio de altura.
    """
    if len(lista) > 0:
        imprimir_dato("El promedio de altura es: {0}".format(calcular_promedio(lista, "altura"))) 
        
    else:
        return -1
    

#stark_calcular_imprimir_promedio_altura(lista_personajes)

#-----------------6.1---------------------
def imprimir_menu():
    """
    Imprimira el menú de opciones por pantalla,
    el cual permite utilizar toda la funcionalidad ya programada
    """
    imprimir_dato("\n       MENU HEROES \n1) Nombre de Superheroes\n2) Altura de cada heroe\n3) SuperHeroe mas alto\n"
                    "4) Superheroe mas bajo\n5) Promedio de altura de los Superheroes\n6) Superhero Mas y Menos pesado:\n7) Salir\n")
    
#imprimir_menu()

#-------------------6.2--------------------
def validar_entero(numero:str)-> bool:
    """
    Recibe por parámetro un string de número el cual deberá
    verificar que sea un string conformado únicamente por dígitos. 
    Retornara True en caso de serlo, False caso contrario
    """
    if numero.isnumeric():
        return True
    
    else:
        return False
    
#------------------6.3---------------    
def stark_menu_principal():
    """
    Se encargará de imprimir el menú de opciones y le pedirá
    al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo.
    En caso de ser correcto dicho número, lo retornara casteado a entero,
    caso contrario retorna -1
    """
    imprimir_menu() 
    respuesta = input("Ingrese un numero de las opciones:\n")
    if validar_entero(respuesta) :
        respuesta = int(respuesta)
        return respuesta
    else:
        return -1

#stark_menu_principal()
 
 #----------------7-------------------
def stark_mavel_app(lista:list):
    """
    Recibe por parámetro una lista y se encargará
    de la ejecución principal de nuestro programa. 
    """
    while True:
        respuesta = stark_menu_principal()
            
        if respuesta == 1:
            stark_imprimir_nombres_heroes(lista)
        elif respuesta == 2:
            stark_imprimir_nombres_alturas(lista)
        elif respuesta == 3:
            stark_calcular_imprimir_heroe(lista, "maximo", "altura")
        elif respuesta == 4:
            stark_calcular_imprimir_heroe(lista, "minimo", "altura")
        elif respuesta == 5:
            stark_calcular_imprimir_promedio_altura(lista)
        elif respuesta == 6:
            stark_calcular_imprimir_heroe(lista,"maximo", "peso")
            stark_calcular_imprimir_heroe(lista,"minimo", "peso")
        elif respuesta == 7:
            break
        else:
            imprimir_dato("Ingreso invalido")
            
        
stark_mavel_app(lista_personajes)
    