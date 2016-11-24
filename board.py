import square
from local import *
class Board():
    # Represents the entire playing field.
    def __init__(self):
        """
        window: main display surface.
        """
        self.sq_list = []        
        # Create squares.
        for x in range(SCREEN_WIDTH/SQ_SIZE):
            temp_ls = []  # To store another column of squares.
            for y in range(SCREEN_HEIGHT/SQ_SIZE):
                temp_ls.append(square.Square(x, y))
            self.sq_list.append(temp_ls)
                
                
    def draw(self):
        for column in self.sq_list:
            for square in column:
                square.draw()
        
        
    
        
    
