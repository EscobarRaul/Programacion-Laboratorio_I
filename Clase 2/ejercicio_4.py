heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"]

heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}


for heroe in heroes_para_reclutar:
    if heroe in heroes_info.keys():
        code_name = heroe
        info_heroe = heroes_info[heroe]
        id_heroe = info_heroe["ID"]
        origen_heroe = info_heroe["Origen"]
        identidad_heroe = info_heroe["Identidad"]
        habilidades_heroe = info_heroe["Habilidades"]

        lista_habilidades = set(habilidades_heroe)
        lista_habilidades_unicas = list(lista_habilidades)
        habilidades_mensaje = " | ".join(lista_habilidades_unicas)

        print("ID:{0} , Codename: {1}\nIdentidad: {2}, Origen: {3}\nHabilidades: {4}\n----------------------------------------------------- ".format(
            id_heroe, code_name, identidad_heroe, origen_heroe, habilidades_mensaje))


#print(heroes_info["Power Girl"])


# for heroe in heroes_para_reclutar:
#     for info_heroe in heroes_info:
#         if heroe == info_heroe:
#             print(heroe)


#print(heroes_info["Super Girl"])


# lista_heroes = []

# for heroe in heroes_info:
#     for nombre in heroes_para_reclutar:
#         if (heroe == nombre):
#             heroes_reclutados = {}#"ID":heroes_info [nombre]["ID"]},#["Habilidades"]}

#             heroes_reclutados["ID"] = heroes_info ["Shazam"]["ID"]
#             heroes_reclutados[heroe] = nombre["Shazam"]
#             heroes_reclutados
#             heroes_reclutados["habilidades"] = heroes_info ["Shazam"]["Habilidades"]

# print("ID: ",her)
