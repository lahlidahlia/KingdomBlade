import tile
from local import *
import math
class Board(object):
    """Represents the entire playing field."""
    tile_list = []
    def __init__(self):
        """
        
        """
        
        
        # Create squares.
        for x in range(BOARD_WIDTH):
            temp_ls = []  # To store another column of squares.
            for y in range(BOARD_HEIGHT):
                temp_ls.append(tile.Tile(x, y))
            Board.tile_list.append(temp_ls)
                
                
    def draw(self):
        for column in Board.tile_list:
            for tile in column:
                tile.draw()
    
    @staticmethod            
    def get_tile_at_pos(pos):
        """
        Return the tile at screen coordinate (x, y)
        Pos is tuple (x, y)       
        """
        return Board.tile_list[int(math.floor(pos[0]/TILE_SIZE))][int(math.floor(pos[1]/TILE_SIZE))]