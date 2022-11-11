import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB

flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=0,y=100,w=300,h=400,color_background=(255,255,0),color_border=(255,0,255),active=True)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=0,y=100,w=300,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False)

while True:     
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    if(form_menu_A.active):
        form_menu_A.update(lista_eventos)
        form_menu_A.draw()

    elif(form_menu_B.active):
        form_menu_B.update(lista_eventos)
        form_menu_B.draw()

    pygame.display.flip()




    


  



