
class Buildings:
    def __init__ (self, x, y, z, id, position): #x,y,z are demensions of the building
        self.x = x
        self.y = y
        self.z = z
        self.id = id
        self.position = {id, position}