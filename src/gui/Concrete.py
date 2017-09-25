
class Config:

    def __init__(self):
        self.size=(0,0)
        self.flocks=0
        self.boids=0
        self.initial_flock_placement=(0,0)
        self.boid_behavior = Boid_Behavior()

    def get_size(self):
        return self.size
    def set_size(self,size):
        self.size=(float(size[0]),float(size[1]))

    def get_flocks(self):
        return self.flocks
    def set_flocks(self,count):
        self.flocks=int(count)

    def get_boids(self):
        return self.boids
    def set_boids(self,count):
        self.boids=count

    def get_initial_flock_placement(self):
        return self.initial_flock_placement
    def set_initial_flock_placement(self,position):
        self.initial_flock_placement=(float(position[0]),float(position[1]))

    def get_boid_behavior(self):
        return self.boid_behavior
    def set_boid_behavior(self,perception,distance,decay):
        self.boid_behavior=Boid_Behavior(perception=0,distance=0,decay=0)


class Boid_Behavior:

    def __init__(self,perception=0,distance=0,decay=0):
        self.perception_radius=perception
        self.distance_weight=distance
        self.decay_weight=decay
