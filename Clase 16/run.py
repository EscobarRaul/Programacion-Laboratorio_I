import pygame
from constantes import *
import tablero

pygame.init() #Se inicializa pygame
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA+100))
pygame.display.set_caption('The Simpsons Memotest')

# FONDO DE JUEGO
fondo = pygame.image.load("Clase 16/recursos/fondo.png")
fondo = pygame.transform.scale(fondo,(ANCHO_PANTALLA,ALTO_PANTALLA+100))
#MUSICA DE FONDO
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("Clase 16/recursos/fondo.wav")
sonido_fondo.set_volume(0.1)
sonido_fondo.play(-1)

#Click en una carta
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_click = pygame.mixer.Sound("Clase 16/recursos/clic.wav")
sonido_click.set_volume(0.1)


#set tick timer 
tick_1s = pygame.USEREVENT+0
pygame.time.set_timer(tick_1s,1000)

tablero_juego = tablero.init()
clock_fps = pygame.time.Clock()

running = True
while running:
    
    clock_fps.tick(60)#inserta FPS
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            tablero.colicion(tablero_juego,event.pos)
            sonido_click.play()
            
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.USEREVENT:
            if event.type == tick_1s:
                #print("Ya paso un segundo")
                pass
    
    tablero.update(tablero_juego)
    # Se pinta el fondo de la ventana de blanco
    pantalla_juego.fill((255, 255, 255))
    # Se dibuja un circulo azul
   # pygame.draw.circle(pantalla_juego, (0, 0, 255), (250, 250), 75)
    # Se dibuja un cuadrado amarillo
    #pygame.draw.rect(pantalla_juego, (255, 255, 0), cuadrado)
    #imagen = pygame.image.load(r"C:\Users\Profesor\Desktop\PL1_PY_2022_2C\clase_16\recursos\01.png")
    #pygame.transform.scale(imagen, (100,100))
   # pantalla_juego.blit(imagen,(50,50))
   # font = pygame.font.SysFont("Arial Narrow", 50)
    #text = font.render("HOLA MUNDO", True, (255, 0, 0))
    #pantalla_juego.blit(text,(100,100))
    # Muestra los cambios en  la pantalla
    
    pantalla_juego.blit(fondo, (0,0))
    tablero.render(tablero_juego,pantalla_juego)
    
    pygame.display.flip()
  
# Done! Time to quit.
pygame.quit()
sonido_fondo.stop()