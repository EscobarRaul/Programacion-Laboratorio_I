import pygame

pygame.init()

ANCHO_VENTANA =  500
ALTO_VENTANA = 500

COLOR_BLANCO = (255,255,255)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_NEGRO = (0,0,0)
COLOR_AZUL = (0,0,255)

ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("PYGAME TEST")
#print(type(ventana_ppal))#<class 'pygame.Surface'>

flag_run = True
pos_circulo = [30,60]

# TIMER
timer_segundo = pygame.USEREVENT
pygame.time.set_timer(timer_segundo, 100)

# LEER UNA IMAGEN
imagen_homero = pygame.image.load("Pygame\homero.png")
imagen_homero = pygame.transform.scale(imagen_homero,(200,200))
rect_homero = pygame.Rect(0, 0, 200, 200)

# CREAR UN TEXTO
fuente = pygame.font.SysFont("Arial", 30)
texto = fuente.render("HOLA HOMERO", True, COLOR_ROJO)


escala = [50,50]

while flag_run:
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN: #Se obtiene la posicion de donde se hace click
            print(evento.pos)# pos : es una tupla que contiene (X,Y)
            pos_circulo = list(evento.pos)
            
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_segundo:
                if pos_circulo[0] < ANCHO_VENTANA + 80: 
                    pos_circulo[0] = pos_circulo[0] + 10
                else:
                    pos_circulo[0] = -80
                    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                pos_circulo[1] = pos_circulo[1] + 100
            # if evento.key == pygame.K_LEFT:
            #     pos_circulo[1] = pos_circulo[1] - 100
    
    lista_teclas = pygame.key.get_pressed()# te devuelve todas las teclas presionadas.
    if lista_teclas[pygame.K_LEFT] :
        pos_circulo[1] = pos_circulo[1] + 1
            
    ventana_ppal.fill(COLOR_VERDE)
    
    pygame.draw.circle(ventana_ppal, COLOR_NEGRO, (pos_circulo), 80)
    
    pygame.draw.rect(ventana_ppal, COLOR_ROJO, rect_homero)# X, Y, ANCHO, ALTO
    ventana_ppal.blit(imagen_homero,rect_homero) #agregamos una imagen
    
    ventana_ppal.blit(texto, (300,300)) # agregamos un texto en pantalla
    
    pygame.display.flip()#el usuario vera los cambios con este flip
    

pygame.quit()#Cierra el juego