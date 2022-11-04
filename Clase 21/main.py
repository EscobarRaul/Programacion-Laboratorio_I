import pygame
import sys
from constantes import *
from player import Player
from plataforma import Platform



screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("Clase 21/images/locations/forest/all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=0,y=400,speed_walk=4,speed_run=8,gravity=8,jump_power=25,frame_rate_ms=80,move_rate_ms=10,jump_height=150)

lista_plataformas = []
lista_plataformas.append(Platform(400,500,50,50,1))
lista_plataformas.append(Platform(480,500,50,50,1))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())

    for plataforma in lista_plataformas:
        plataforma.draw(screen)


    player_1.events(delta_ms,keys)
    player_1.update(delta_ms,lista_plataformas)
    player_1.draw(screen)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    #print(delta_ms)



    






