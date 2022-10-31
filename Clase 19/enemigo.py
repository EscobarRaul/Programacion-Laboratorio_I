import pygame
from constantes import *
from auxiliar import Auxiliar

# def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False,step=1):
#     lista = []
#     surface_imagen = pygame.image.load(path)
#     fotograma_ancho = int(surface_imagen.get_width()/columnas)
#     fotograma_alto = int(surface_imagen.get_height()/filas)
#     for columna in range(0,columnas,step):
#         for fila in range(filas):
#             x = columna * fotograma_ancho
#             y = fila * fotograma_alto
#             surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
#             if flip:
#                 surface_fotograma = pygame.transform.flip(surface_fotograma, True, False)
#             lista.append(surface_fotograma)
#     return lista

class Enemigo:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump):
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 19/images/caracters/green_hat/walk.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 19/images/caracters/green_hat/walk.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 19/images/caracters/green_hat/idle.png",16,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 19/images/caracters/green_hat/idle.png",16,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 19/images/caracters/green_hat/jump.png",33,1,False,2)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/raule/OneDrive/Escritorio/raul UTN/Programacion-Laboratorio_I/Clase 19/images/caracters/green_hat/jump.png",33,1,True)
        self.frame = 0
        self.move_x = x
        self.move_y = y
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump = jump
        
        self.is_jump = False
        
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        
        #atributos para el salto
        self.impulso=10
        self.is_jump = False
        
    def control(self,action):
        if(action == "WALK_R"):
            self.move_x = self.speed_walk
            self.animation = self.walk_r
            self.frame = 0
            
        elif(action == "WALK_L"):
            self.move_x = - self.speed_walk
            self.animation = self.walk_l
            self.frame = 0
        
        elif(action == "JUMP"):
            if self.is_jump:
                if self.impulso >= -10: # -10 es el limite inferior del salto
                    if self.impulso < 0: # menor que 0 significa que va en bajada el salto
                        self.move_y += (self.impulso**2)*0.5 # (**2) elevado a la 2 divido 2 (0.5)
                    else:
                        self.move_y -= (self.impulso**2)*0.5 # aca estaria de subida por que se le debe disminuir la Y
                    self.impulso -= 1 # se hace esto para que el salto llegue a -10 por eso se hace afuera del if
                else: # impulso salto no sea mayor igual a 10, termina el salto
                    self.is_jump = False
                    self.impulso = 10
            else:
                if self.move_y > self.speed_walk:#ir hacia arriba
                    self.move_y -= self.speed_walk
                if self.move_y < self.speed_walk:#ir hacia abajo
                    self.move_y += self.speed_walk
                if (action == "JUMP"):
                    self.is_jump=True
        
        # elif(action == "JUMP_R"):
        #     self.move_y = self.jump
        #     self.move_x = self.speed_walk
        #     self.animation = self.jump_r
        #     self.frame = 0
        #     self.is_jump = True
            
        # elif(action == "JUMP_L"):
        #     self.move_y = - self.jump
        #     self.move_x = self.speed_walk
        #     self.animation = self.jump_l
        #     self.frame = 0
        #     self.is_jump = True
            
        elif(action == "STAY_R"):
            self.animation = self.stay_r
            self.frame = 0
            self.move_x = 0
            self.move_y = 0
            
        elif(action == "STAY_L"):
            self.animation = self.stay_l
            self.frame = 0
            self.move_x = 0
            self.move_y = 0
            
            
    def update(self):
        if(self.frame < len(self.animation)-1):
            self.frame += 1
        else:
            self.frame = 0
            if(self.is_jump == True):
                self.is_jump = False
                self.move_y = 0
                
        
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        
        if(self.rect.y < 500):
            self.rect.y += self.gravity
        
    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        
        
        
        
        
        
        

        
























        
    # def draw(self,screen):
    #     self.move()
    #     if sel
        
        
        
    # def move(self):
    #     if self.vel > 0:
    #         if self.x < self.walk_r + self.vel:
    #             self.x += self.vel
    #         else:
    #             self.vel = self.vel * -1
    #             self.x += self.vel
    #             self.walkCount = 0
    #     else:
    #         if self.x > self.walk_l - self.vel:
    #             self.x += self.vel
    #         else:
    #             self.vel = self.vel * -1
    #             self.x += self.vel
    #             self.walkCount = 0
                
        