import pygame
from auxiliar import Auxiliar
from constantes import *


class Enemigo:
    def __init__(self,x,y,limite):
        self.x = x
        self.y = y
        self.velocidad = 5
        self.stay =  Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego/img/villano/idle.png", 15,9)
        self.stay_l =  Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego/img/villano/idle.png", 15,9,True)
        self.frame = 0
        self.camino = [self.x,limite]
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego/img/villano/walk.png", 3,6)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("Prueba_Juego/img/villano/walk.png", 3,6,True)
        self.move_l = True
        self.move_r = True
        
    
    def draw(self,ventana):
        #se agrega un rango de frames para que no pase la del sprite
        if self.frame + 1 > len(self.stay) or self.frame + 1 > len(self.walk_l) or self.frame + 1 > len(self.walk_r):
            self.frame = 0
        if self.move_l:
            ventana.blit(self.walk_l [self.frame],(self.x,self.y))
            self.frame += 1
        elif self.move_r:
            ventana.blit(self.walk_r [self.frame],(self.x,self.y))
            self.frame += 1
            
        else:
            ventana.blit(self.stay[self.frame],(self.x,self.y))#Se dibuja al villano quieto
            self.frame += 1
        
    
    def se_mueve_solo(self):
        if self.velocidad > 0:
            if self.x + self.velocidad < self.camino[1]:
                self.x += self.velocidad
                self.move_r = False
                self.move_l = True
            else:
                self.velocidad = self.velocidad * -1
                self.frame = 0
        else:
            if self.x - self.velocidad > self.camino[0]:
                self.x += self.velocidad
                self.move_l = False
                self.move_r = True
            else:
                self.velocidad = self.velocidad * -1
                self.frame = 0
                
            
        
    # def update(self):
    #     if(self.frame < len(self.stay) - 1):
    #         self.frame += 1 
    #     else: 
    #         self.frame = 0
        