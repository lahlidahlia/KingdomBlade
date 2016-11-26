from local import *
from board import Board
import a_star
import pdb

class Squad(object):
    """
    Represents a squad of units.
    Is an abstract to be derived from. Do not instantiate this.
    """
    def __init__(self, x, y, amount):
        # Do not have to be implemented.
        # self.x = x
        # self.y = y
        self.amount = amount  # Amount of units this squad has. Remains the same even if split.
        
        self.speed = None  # In m/s.
        self.move_mode = None  # Walking, running, etc...
        
        # Tile setup
        self.main_tile = Board.tile_list[x][y]  # Which tile is this unit based on?
        # Give information to the tile.
        self.main_tile.squad = self  
        self.main_tile.amount = self.amount
        self.other_tile = None  # The other tile that the squad stands on (if split, can only split to one other tile).
        self.dest_tile = None  # Squad will move toward dest_tile if provided.
        self.path = []  # If the squad is moving then there will be a path to take.
        self.next_tile = None  # Next tile to move into (not destination).
        self.next_finish = True  # The squad finished moving to the next square (not destination).
        
        
        
        # Please implement these values.
        self.maxAmount = None  # Maximum unit allowed on a square. Can be seen as density when calculating speed.
        self.attack = None
        self.health = None  # ??? May not be necessary.
        self.defense = None
        self.base_speed = None  # Speed before move_mode modifier.
        self.color = None
        
        
    def loop(self):
        """Executed every frame."""
        self.speed = self.base_speed

        if self.dest_tile:
            if self.next_finish:
                print("Popping!")
                self.next_tile = self.path.pop()
                self.next_finish = False
            
            move_left = self.get_move_amount
            while move_left:
                # Move the unit until can't anymore for the tick.
                move_left = self.move(self.next_tile.x - self.main_tile.x, self.next_tile.y - self.main_tile.y, move_left)
            if self.amount == self.main_tile.amount:
                self.next_finish = True
                if self.main_tile == self.dest_tile:  # We've reached our destination.
                   self.stop_moving()

    
    def set_destination(self, dest_tile):
        """Set a destination for this squad to travel toward."""
        self.dest_tile = dest_tile
        self.path = a_star.construct_path(self.main_tile, self.dest_tile)
        self.next_tile = None
        self.next_finish = True
    
    
    def stop_moving(self):
        """Stop the unit from moving"""
        self.dest_tile = None
        self.path = []
        self.next_tile = None
        self.next_finish = True
    
    
    def move(self, dx, dy, available_movement):
        """
        Move one square in any direction (does not support diagonal movement)
        If both dx and dy != 0 then only move in the x direction.

        available_movement: max amount of units that can move this turn.
        
        If there is unit movement still available, return amount of units that can move. Otherwise just 0.
        """
        # Normalized these values.  (Unit can't try to move more than 1 square at once.)
        #pdb.set_trace()
        dx = sign(dx)  
        dy = sign(dy)
        if dx and dy:  # Ignore y movement if both was given.
            dy = 0
            
        dest_tile = Board.tile_list[self.main_tile.x + dx][self.main_tile.y + dy]  # Temp variable.
        print("dest: {}, {}".format(dest_tile.x, dest_tile.y))
        move_amount = self.get_move_amount()
        move_amount = move_amount if move_amount < available_movement else available_movement
        #print move_amount
        if not self.other_tile:  # If squad isn't already split. Moves differently if so.
            if move_amount >= self.amount:  # If moving all units.
                self.main_tile.reset()  # Remove this squad's information from the tile.
                dest_tile.squad = self
                dest_tile.amount = self.amount
                self.main_tile = dest_tile
                return move_amount - self.amount
            else:  # Partial move
                if self.main_tile == dest_tile:
                    return 0
                self.main_tile.amount -= move_amount
                dest_tile.squad = self
                dest_tile.amount = move_amount
                self.other_tile = self.main_tile
                self.main_tile = dest_tile
                return 0
        else:  # If squad is already split.
            if dest_tile == self.other_tile:  # If trying to move back to previous tile.
                if move_amount >= self.main_tile.amount:  # Moving all units to previous square.
                    move_remaining = move_amount - self.main_tile.amount  # Remaining units available to move.
                    self.other_tile.amount = self.amount
                    self.main_tile.reset()
                    self.main_tile = self.other_tile
                    self.other_tile = None  # Squad is unified.
                    return move_remaining
                else:  # Partial move.
                    print("!!!!!!!!!")
                    self.main_tile.amount -= move_amount
                    dest_tile.amount += move_amount
                    # Swapping main tile.
                    self.other_tile = self.main_tile  
                    self.main_tile = dest_tile
                    return 0
            else:  # Moving to any other tiles.
                # Units have to be unified before moving to a new tile.
                # Thus this unifies them.
                if move_amount >= self.other_tile.amount:  # Move all units.
                    move_remaining = move_amount - self.other_tile.amount
                    self.main_tile.amount = self.amount
                    self.other_tile.reset()
                    self.other_tile = None
                    return move_remaining
                else:  # Partial move.
                    self.other_tile.amount -= move_amount
                    self.main_tile.amount += move_amount
                    return 0
            
    def get_move_amount(self):
        """Calculate how many units to move given the speed of the unit."""
        ret = (float(self.speed) / TILE_DISTANCE * self.maxAmount) / FPS
        #print("Move amount: {}".format(ret))
        return ret
    
        