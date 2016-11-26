import squad
from local import *

class Infantry(squad.Squad):
    """
    Infantry: standard ground unit.
    """
    def __init__(self, x, y, amount):
        super(Infantry, self).__init__(x, y, amount)
        self.maxAmount = 50
        self.attack = 1
        self.health = 10
        self.defense = 1
        self.base_speed = 10
        self.color = RED_COLOR
        
    