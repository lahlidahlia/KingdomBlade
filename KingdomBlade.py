import pygame
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Kingdom Blade")

whiteColor = pygame.Color(255, 255, 255)
greenColor = pygame.Color(0, 255, 0)

while True:
    window.fill(whiteColor)
    
    pygame.draw.rect(window, greenColor, (20, 20, 40, 40))
    
    # EVENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    pygame.display.update()
    fpsClock.tick(60)
    