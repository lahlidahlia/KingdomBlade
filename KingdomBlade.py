import pygame
import pygame.gfxdraw
import board
import sys
import infantry
from pygame.locals import *
from local import *
import a_star

pygame.init()

fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Kingdom Blade")

Board = board.Board()

dest_tile = None  # (x, y)

Infantry = infantry.Infantry(2, 2, 50)
pygame.key.set_repeat(1, 1)
while True:
    # GAME LOOP
    
    
    
    # EVENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_LEFT:
                move_left = Infantry.move(-1, 0)
            if event.key == K_RIGHT:
                move_left = Infantry.move(1, 0)
            if event.key == K_UP:
                move_left = Infantry.move(0, -1)
            if event.key == K_DOWN:
                move_left = Infantry.move(0, 1)
                path = a_star.construct_path(board.Board.tile_list[5][5], board.Board.tile_list[7][8])
                for tile in path:
                    infantry.Infantry(tile.x, tile.y, 50)
        
        # if event.type == MOUSEBUTTONDOWN:
        #     move_left = 0
        #     if event.button == 3:  # Right MB
        #         
        #     elif event.button == 1:  # Left MB
        #         move_left = Infantry.move(-1, 0)
        #     print("Movement left: {}".format(move_left))
            
    
    # DRAW LOOP
    Infantry.loop()
    window.fill(WHITE_COLOR)
    Board.draw()
    
    pygame.display.update()
    fpsClock.tick(FPS)
    