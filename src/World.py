from Timer import Timer
class World:

    def __init__ (self,x, y, z, buildings):
        self.x = x
        self.y = y
        self.z = z
        self.buildings = buildings
        self.timer = Timer()