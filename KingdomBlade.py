import pygame
import pygame.gfxdraw
import board
import sys
from pygame.locals import *
from local import *

pygame.init()

fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Kingdom Blade")

Board = board.Board()
print(Board)

while True:
    window.fill(WHITE_COLOR)
    #pygame.draw.rect(window, GREEN_COLOR, (20, 20, 40, 40))
    
    # DRAW
    Board.draw()
    
    # EVENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    
    
    pygame.display.update()
    fpsClock.tick(60)
    