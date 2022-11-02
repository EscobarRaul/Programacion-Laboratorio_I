import pygame
from constantes import *
from auxiliar import *
from player import Personaje
from enemy import Enemigo

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("JUEGO")
clock = pygame.time.Clock()

#Se agrega imagen de fondo
imagen_fondo = pygame.image.load("Prueba_Juego/img/all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

#variables del personaje
# x = int(ANCHO_VENTANA/2)
# y = int(ALTO_VENTANA/2)
# pj_stay = Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego\img\idle.png", 16,1)
# pj_walk_r = Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego\img\walk.png", 15,1)
# alto = pj_stay.get_height()
# ancho = pj_stay.get_width()

# frame = 0
# animation = pj_stay
# image = animation[frame]
# rect = image.get_rect()
# velocidad = 5

#Creación Personaje
player_1 = Personaje(int(ANCHO_VENTANA/2),int(ALTO_VENTANA/2))
#Creación Enemigo
enemigo = Enemigo(0, int(ALTO_VENTANA/2),int(ANCHO_VENTANA/2))

running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            quit()
    
    #Evento de movimiento de personaje
    teclas = pygame.key.get_pressed()
    player_1.accion(teclas,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_SPACE)
    
    clock.tick(FPS)
    ventana.blit(imagen_fondo,imagen_fondo.get_rect())
    # ventana.blit(image,(x,y))
    player_1.draw(ventana)
    player_1.update()
    
    enemigo.draw(ventana)
    enemigo.se_mueve_solo()
    # enemigo.update()
    
            
    
    
    pygame.display.flip() # pygame.display.update()

pygame.quit()
