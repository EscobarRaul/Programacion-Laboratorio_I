

# listas.

pokemones  = [
    "mewtwo", # 0
    "moltres", # 1
    "pikachu", # 2
    "charmander" # 3
    # 4 elementos
]

# Append
# Agrega un elemento a la lista [al final de la lista]

print("Lista antes de agregar: {0}".format(pokemones))

pokemones.append("bulbasaur") #! 5 elementos

print("Lista despues de agregar: {0}".format(pokemones))

# Recorrer lista
"""
1- Posee indices donde estaran ubicados los elementos que contendra
2- Los indices son numericos
3- Los indices son en base 0
4- Los indices iran del 0 hasta cantidad elementos -1
"""
# for clasico
print("For clasico")
for indice in range(0,len(pokemones)):
    print(pokemones[indice])

#for-each
print("\nFor Each")    
for pokemon in pokemones:
    print(pokemon)
    