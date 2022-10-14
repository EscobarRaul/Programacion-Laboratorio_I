import pygame
import colores
import random

def crear(x,y,ancho,alto):
    # Leer una imagen
    imagen_dona = pygame.image.load("00.png")
    imagen_dona = pygame.transform.scale(imagen_dona,(ancho,alto))
    rect_dona = imagen_dona.get_rect()
    rect_dona.x = x
    rect_dona.y = y
    dict_dona = {}
    dict_dona["surface"] = imagen_dona
    dict_dona["rect"] = rect_dona
    dict_dona["visible"] = True
    dict_dona["speed"] = random.randrange (10,20,1)
    return dict_dona

def update(lista_donas):
    for dona in lista_donas:
        rect_dona = dona["rect"]
        rect_dona.y = rect_dona.y + dona["speed"]


def actualizar_pantalla(lista_donas,personaje,ventana_ppal):
    for dona in lista_donas:
        if(personaje["rect"].colliderect(dona["rect"])):
            personaje["score"] = personaje["score"] + 100
            restar_dona(dona)
        
        if(dona["rect"].y > 880):
            restar_dona(dona)
        ventana_ppal.blit(dona["surface"],dona["rect"])

    font = pygame.font.SysFont("Arial Narrow", 50)
    text = font.render("SCORE: {0}".format(personaje["score"]), True, (255, 0, 0))
    ventana_ppal.blit(text,(0,0))

def crear_lista_donas(cantidad):
    lista_donas = []
    for i in range(cantidad):
        y = random.randrange (-1000,0,60)
        x = random.randrange (0,740,60)
        lista_donas.append(crear(x,y,60,60))
    return lista_donas

def restar_dona(dona):
    dona["rect"].x = random.randrange (0,740,60)
    dona["rect"].y = random.randrange (-1000,0,60)
