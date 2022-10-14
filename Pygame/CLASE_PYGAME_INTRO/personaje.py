import re
import pygame
import colores

def crear(x,y,ancho,alto):
    dict_personaje = {}
    dict_personaje["surface"] = pygame.image.load("01.png")
    dict_personaje["surface"] = pygame.transform.scale( dict_personaje["surface"],(ancho,alto))
    dict_personaje["rect_pos"] = pygame.Rect(x,y,200,200)
    dict_personaje["rect"] = pygame.Rect((x+ancho/2)-10,y+90,40,20)
    dict_personaje["score"] = 0
    return dict_personaje

def actualizar_pantalla(personaje,ventana_ppal):
    ventana_ppal.blit(personaje["surface"],personaje["rect_pos"])
    #pygame.draw.rect(ventana_ppal,colores.ROJO,personaje["rect"])

def update(personaje,incremento_x):
    nueva_x = personaje["rect_pos"].x + incremento_x
    if(nueva_x > 0 and nueva_x < 600):
        personaje["rect_pos"].x = personaje["rect_pos"].x + incremento_x
        personaje["rect"].x = personaje["rect"].x + incremento_x

