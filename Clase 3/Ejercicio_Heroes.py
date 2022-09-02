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

#------A)-----------
#print(lista_personajes)

#-------B)---------
# for heroe in lista_personajes :
#     print(heroe["nombre"])

#-------C)---------
# for heroe in lista_personajes :
#     print(heroe["nombre"], heroe["altura"])
    
#-------D) HEROE MAS ALTO----------
heroe_mas_alto = lista_personajes[0]
for heroe in lista_personajes:
    heroe_float = float(heroe["altura"])
    heroe_mas_alto_float = float(heroe_mas_alto["altura"])
    if(heroe_float > heroe_mas_alto_float):
        heroe_mas_alto = heroe
        
#print(heroe_mas_alto["altura"])
print("Nombre: {1} - Altura: {0}".format(heroe_mas_alto["altura"],heroe_mas_alto["nombre"])) 


#---------E) HEROE MAS BAJO ----------
heroe_mas_bajo = lista_personajes[0]
for heroe in lista_personajes:
    heroe_float = float(heroe["altura"])
    heroe_mas_bajo_float = float(heroe_mas_bajo["altura"])
    if(heroe_float < heroe_mas_bajo_float):
        heroe_mas_bajo = heroe
        
print("Nombre: {1} - Altura: {0:}".format(heroe_mas_bajo["altura"],heroe_mas_bajo["nombre"])) 
