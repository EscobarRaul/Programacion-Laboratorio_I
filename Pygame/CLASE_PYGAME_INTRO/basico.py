from lib2to3 import pygram
import pygame
import colores
import dona
import personaje
import enemigo

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("PYGAME HOMERO COME DONAS")

#SONIDO DE FONDO
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("Pygame/CLASE_PYGAME_INTRO/sonido_fondo.mp3")

#FONDO
background = pygame.image.load("Pygame/CLASE_PYGAME_INTRO/fondo_nubes.png")
background = pygame.transform.scale(background,(800,800))
# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

timer_dona = pygame.USEREVENT
pygame.time.set_timer(timer,500)


player = personaje.crear(ANCHO_VENTANA/2,ALTO_VENTANA-200,200,200)
lista_donas = dona.crear_lista_donas(20)
dona_mala = enemigo.crear_lista_donas(2)

flag_run = True
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                dona.update(lista_donas)

        if evento.type == pygame.USEREVENT:
            if evento.type == timer_dona:
                dona.update(dona_mala)

    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_LEFT] :
        personaje.update(player,-10)
    if lista_teclas[pygame.K_RIGHT] :
        personaje.update(player,10)

    #ventana_ppal.fill(background)
    ventana_ppal.blit(background,(0,0))
    personaje.actualizar_pantalla(player,ventana_ppal)
    dona.actualizar_pantalla(lista_donas,player,ventana_ppal)
    enemigo.actualizar_pantalla(lista_donas,player,ventana_ppal)

    pygame.display.flip()
    sonido_fondo.set_volume(0.2)
    sonido_fondo.play()
    
pygame.quit()