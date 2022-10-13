import pygame

pygame.init()

running = True

window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Vamos hacer un juego!")
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False