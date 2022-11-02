import pygame
from auxiliar import Auxiliar
from constantes import *


class Personaje:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.stay =  Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego\img\heroe\idle.png", 16,1)
        self.stay_l =  Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego\img\heroe\idle.png", 16,1,True)
        self.velocidad = 5
        self.frame = 0
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        #ATRIBUTOS PARA EL SALTO
        self.impulso_salto = 10
        self.is_jump = False
        #ATRIBUTOS PARA ANIMACIÓN
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego\img\heroe\walk.png", 15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego\img\heroe\walk.png", 15,1,True)[:12]
        self.move_l = False
        self.move_r = False
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego\img\heroe\jump.png",33,1,False)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego\img\heroe\jump.png",33,1,True)
        self.salto_r = False
        self.salto_l = False
        self.contador_pasos = 0
        #NIVEL DE VIDA
        self.salud = 10
        
    def draw(self,ventana):
        if self.contador_pasos + 1 > len(self.walk_r) or self.contador_pasos +1 > len(self.walk_l) :
            self.contador_pasos = 0 
        # if self.salto_r:
        #     ventana.blit(self.jump_r[self.contador_pasos],(self.x,self.y))
        #     self.contador_pasos += 1
        # elif self.salto_l:
        #     ventana.blit(self.jump_l[self.contador_pasos],(self.x,self.y))
        #     self.contador_pasos += 1 
        if self.move_l:
            ventana.blit(self.walk_l [self.contador_pasos],(self.x,self.y))
            self.contador_pasos += 1
            self.animation = self.stay_l # Una vez que el pj va hacia la izquierda se quedara viendo a ese lado
        elif self.move_r:
            ventana.blit(self.walk_r [self.contador_pasos],(self.x,self.y))
            self.contador_pasos += 1
            self.animation = self.stay
        else:
            self.image = self.animation[self.frame]
            ventana.blit(self.image,(self.x,self.y))

        #Creando barra de vida
        pygame.draw.rect(ventana,(255,0,0),(self.x+20, self.y - 20, 50,10))
        pygame.draw.rect(ventana,(0,128,0),(self.x+20, self.y - 20, 50 -(5 * (10 - self.salud)),10))
                         
    def accion(self, k, iz, de, ar, ab,salta):
        #Izquierda
        if k[iz] and self.x > self.velocidad:
            self.x -= self.velocidad
            #Controles de animacion
            self.move_l = True
            self.move_r = False
            
        #Derecha
        elif k[de]and self.x < ANCHO_VENTANA - self.stay[0].get_width()-self.velocidad:
            self.x += self.velocidad
            #Controles de animacion
            self.move_r = True
            self.move_l = False
            
        else:
            #Controles de animacion en caso de dejar de moverse en horizontal
            self.move_r = False
            self.move_l = False
            self.salto_r = False
            self.salto_l = False
            self.contador_pasos = 0
        
        #Control del salto
        if self.is_jump:
            if self.impulso_salto >= -10: # -10 es el limite inferior del salto y nos permite no caer mas abajo del punto donde salto
                if self.impulso_salto < 0: # menor que 0 significa que va en bajada
                    self.y += (self.impulso_salto**2)/2 #esto hace referencia a una funcion cuadratica de una parabola
                else:
                    self.y -= (self.impulso_salto**2)/2 #va en subida el salto
                self.impulso_salto -= 1 # aca se va restando el salto para que llegue a 10
            else:# cuando el salto ya no sea menor a 10, osea que el salto llego a su fin
                self.is_jump = False
                self.impulso_salto = 10
        else:#si no se activa la tecla del salto, el pj se movera hacia arriba o abajo
            #Arriba
            if k[ar] and self.y > self.velocidad:
                self.y -= self.velocidad
            #Abajo
            if k[ab] and self.y < ALTO_VENTANA - self.stay[0].get_height()-self.velocidad:
                self.y += self.velocidad
            #Salta
            if k[salta]:# se agrega la tecla del salto, para volver al if del salto.
                self.is_jump = True
                #Controles de animación
                self.salto_r = True
                self.salto_l = True
                self.move_r = False
                self.move_l = False
                
                
            
    def update(self):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0
        