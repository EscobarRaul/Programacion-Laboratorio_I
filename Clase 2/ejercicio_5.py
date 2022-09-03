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

dic_habilidades = {}
habilidades_utn = []

for habilidad in habilidades:
    habilidades_utn=[]
    for dato in habilidad:
        habilidades_utn.append(habilidad[dato])
        
    print(habilidades_utn)
