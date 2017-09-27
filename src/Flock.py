
import Boid


class Flock:
    flockcount = 0
    
    def __init__(self, num_boids, center, radius): #possibly also orientation, maybe something about obstacles?
        self.num_boids = num_boids
        self.center = center
        self.radius = radius
        self.boid_list = []
        self.flockcount += 1
        self.distance_matrix = []
        
        
        for i in range(num_boids):
            boid_list.append(Boid(ident, position, vel, acc))
        
        
    def update(self):
        return self.boid_list
    
    
    def dist_matrix(self):
        for i in range(len(self.boid_list)):
            for j in range(len(self.boid_list)-i):
                self.boid_pos = something
        return 0