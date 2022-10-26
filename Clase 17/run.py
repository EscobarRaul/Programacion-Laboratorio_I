import pygame
from constantes import *
import tablero

pygame.init() #Se inicializa pygame
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('The Simpsons Memotest')

tick_1s = pygame.USEREVENT+0
pygame.time.set_timer(tick_1s,1000)

tick_1500ms = pygame.USEREVENT+1
pygame.time.set_timer(tick_1500ms,1500)

tablero_juego = tablero.init()
clock_fps = pygame.time.Clock()
running = True
while running:
    tiempo = clock_fps.tick(60)
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            tablero.colicion(tablero_juego,event.pos)
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == tick_1s:
            print("Ya paso un segundo")
            pass
        if event.type == tick_1500ms:
            print("Ya pasaron 1500ms")
            pass
    tablero.update(tablero_juego)
    # Se pinta el fondo de la ventana de blanco
    pantalla_juego.fill((255, 255, 255))
    tablero.render(tablero_juego,pantalla_juego)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()