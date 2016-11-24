import unit

class Infantry(unit.Unit):
    """
    Infantry: standard ground unit.
    """
    def __init__(self):
        super(Infantry, self).__init__()
        self.maxAmount = 50
        self.attack = 1
        self.health = 10
        self.defense = 1
        self.base_speed = 1
        
    