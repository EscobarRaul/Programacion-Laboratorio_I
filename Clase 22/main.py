import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from plataforma import Plataform 

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("Clase 22/images/locations/set_bg_01/forest/all.png").convert()

imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=0,y=400,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)
plataform_list = []
plataform_list.append(Plataform(x=400,y=500,width=50,height=50,type=0))
plataform_list.append(Plataform(x=450,y=500,width=50,height=50,type=1))
plataform_list.append(Plataform(x=500,y=500,width=50,height=50,type=2))   
plataform_list.append(Plataform(x=600,y=430,width=50,height=50,type=12))
plataform_list.append(Plataform(x=650,y=430,width=50,height=50,type=14))
plataform_list.append(Plataform(x=750,y=360,width=50,height=50,type=12))
plataform_list.append(Plataform(x=800,y=360,width=50,height=50,type=13))
plataform_list.append(Plataform(x=850,y=360,width=50,height=50,type=13))
plataform_list.append(Plataform(x=900,y=360,width=50,height=50,type=14))
         
while True:     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())

    for plataforma in plataform_list:
        plataforma.draw(screen)

    player_1.events(delta_ms,keys)
    player_1.update(delta_ms,plataform_list)
    player_1.draw(screen)
    #print(delta_ms)
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    #print(delta_ms)



    


  



