
class Config:

    def __init__(self):
        return True


class Config_World:

    def __init__(self,screen, objects,flocks):
        #init
        return True

class Config_Screen:
    def __init__(self, x_pos, y_pos, x_size, y_size):
        return True

class Config_Static_Object:

    def __init__(self):
        return True

class Config_Flock:

    def __init__(self,boids = None,center = None, radius = None):
        self.boids = boids
        self.center = center
        self.radius = radius

class Config_Boid:

    behaviors = ()

    def __init__(self, parent, id, velocity_max, velocity, position, behavior):
        self.parent = parent
        self.id = id
        self.velocity=velocity
        self.position = position
        self.velocity_max=velocity_max
        self.behavior = behavior

class Config_Behavior:

    def __init__(self, id, neighbor = 0, center = 0, direction = 0):
        self.id
        self.neighbor_weight = neighbor
        self.center_weight = center
        self.direction_weight = direction