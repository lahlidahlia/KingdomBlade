import pygame
import pygame.gfxdraw
from local import *
class Square():    
    # Represents individual squares.
    def __init__(self, x, y, color=RED_COLOR):
        """
        window: main display surface.
        """
        self.unit = None  # Which unit is on this tile.
        self.type = None  # What type of terrain is it.
        self.amount = 0  # If there's a unit then how many?
        self.x = x
        self.y = y
        self.surface = pygame.Surface((SQ_SIZE, SQ_SIZE))
        
    def draw(self):
        from kingdomBlade import window
        color = None
        
        # Draw the fill.
        if self.unit:  # If there is a unit on this tile.
            color = RED_COLOR #TODO: Put unit's color here.
            #color.a = #TODO: Put unit's transparency here.
            pygame.gfxdraw.box(window, (self.x * SQ_SIZE, self.y * SQ_SIZE, SQ_SIZE, SQ_SIZE), color)
        
        # Draw the border.
        color = BLACK_COLOR
        color.a = 255
        pygame.gfxdraw.rectangle(window, (self.x * SQ_SIZE, self.y * SQ_SIZE, SQ_SIZE, SQ_SIZE), color)
        
        
        
    
        
