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
        self.x = x
        self.y = y
        self.cost = 1
        
        # Implement these variables
        self.type = None  # What type of terrain is it.
        
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
        
        font = pygame.font.SysFont("monospace", 10)
        text = font.render("{},{}".format(self.x, self.y), True, BLACK_COLOR)
        window.blit(text, (self.x*TILE_SIZE + 2, self.y*TILE_SIZE+2))
        
        
    def set_squad(self, squad, amount):
        """ Set the squad's information for this tile."""
        self.squad = squad
        self.amount = amount
    
        
    def reset(self):
        """Reset squad and amount values on this tile."""
        self.squad = None
        self.amount = None
    
        
    def get_neighbors(self):
        from board import Board
        """Return a list of adjacent tiles."""
        ret = []
        #print({}, {})
        if self.x > 0:
            ret.append(Board.tile_list[self.x - 1][self.y])
        if self.x < BOARD_WIDTH-1:
            ret.append(Board.tile_list[self.x + 1][self.y])
        if self.y > 0:
            ret.append(Board.tile_list[self.x][self.y - 1])
        if self.y < BOARD_HEIGHT-1:
            ret.append(Board.tile_list[self.x][self.y + 1])
            
        return ret
    
        
