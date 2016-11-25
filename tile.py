import pygame
import pygame.gfxdraw
from local import *
class Tile(object):    
    # Represents individual squares.
    def __init__(self, x, y, color=RED_COLOR):
        """
        
        """
        # Squad variables
        self.squad = None  # Which squad is on this tile.
        self.amount = 0  # If there's a squad then how many units?
        
        # Tile information variables
        self.type = None  # What type of terrain is it.
        self.x = x
        self.y = y
        
        #self.surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
        
        
    def draw(self):
        from kingdomBlade import window
        color = None
        
        # Draw the fill.
        if self.squad:  # If there is a squad on this tile.
            color = self.squad.color
            color.a = int((float(self.amount) / self.squad.maxAmount) * 255)  # Tile transparency
            pygame.gfxdraw.box(window, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE), color)
        
        # Draw the border.
        color = BLACK_COLOR
        color.a = 255
        pygame.gfxdraw.rectangle(window, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE), color)
        
        
    def set_squad(self, squad, amount):
        """ Set the squad's information for this tile."""
        self.squad = squad
        self.amount = amount
    
        
    def reset(self):
        """Reset squad and amount values on this tile."""
        self.squad = None
        self.amount = None
    
        
    
        
