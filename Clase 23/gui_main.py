import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_button import Button 
from gui_form import FormMenu

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()


form_menu = FormMenu(master_surface=screen,x=200,y=200,w=1000,h=800,color_background=(255,255,0),color_border=(255,0,255),active=True)

while True: 
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    if(form_menu.active): # si esta activo se dibuja en pantalla
        form_menu.update(lista_eventos)
        form_menu.draw()

    pygame.display.flip()
    