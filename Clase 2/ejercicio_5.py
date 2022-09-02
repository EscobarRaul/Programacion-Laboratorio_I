habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]

habilidades_utn = []
dic_habilidades = {}
for habilidad in habilidades:
    hab_utn = []
    for dato in habilidad:
        hab_utn.append(habilidad[dato])
        
    

print(hab_utn)