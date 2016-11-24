def Unit():
    """
    Represents a square of unit.
    Is an abstract to be derived from. Do not instantiate this.
    """
    def __init__(self, x, y):
        # Please implement these values.
        self.maxAmount = None  # Maximum unit allowed on a square.
        self.attack = None
        self.health = None  # ??? May not be necessary.
        self.defense = None
        self.base_speed = None  # Speed before move_mode modifier.
        
        # Do not have to be implemented.
        self.tile = None  # Which tile is this unit on?
        self.speed = None  # In m/s.
        self.move_mode = None  # Walking, running, etc...
        