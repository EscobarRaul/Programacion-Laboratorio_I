#from curses import KEY_DOWN
import pygame
import sys
from constantes import *
from player import Player
from enemigo import Enemigo

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("Clase 19/images/locations/forest/all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player_1 = Player(0,0,4,8,8,16)

#enemigo = Enemigo(0,0,4,8,8,16)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #enemigo.control("WALK_L")
                player_1.control("WALK_L")
            if event.key == pygame.K_RIGHT:
                #enemigo.control("WALK_R")
                player_1.control("WALK_R")
            if event.key == pygame.K_SPACE:
                #enemigo.control("JUMP_R")
                player_1.control("JUMP_R")
        if event.type == pygame.KEYUP:
            # if event.key == pygame.K_LEFT:
            #     enemigo.control("STAY_L")
            # if event.key == pygame.K_RIGHT:
            #     enemigo.control("STAY_R")
            # if event.key == pygame.K_SPACE:
            #     enemigo.control("STAY_R")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                player_1.control("STAY")

    screen.blit(imagen_fondo,imagen_fondo.get_rect())
   
    player_1.update()
    player_1.draw(screen)
    # enemigo.update()
    # enemigo.draw(screen)
    
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)



    






