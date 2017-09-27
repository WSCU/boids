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
        
        row = -1
        for i in range(num_boids):
            if i % 10 == 0:
                row += 1
            self.boid_list.append(Boid(i, (200 - 10*row, -20 + 4*i, 50), (-22, 0, 0), 0))
        
        
    def update(self):
        return self.boid_list
    
    
    def dist_matrix(self):
        for i in range(len(self.boid_list)):
            for j in range(len(self.boid_list)-i):
                # self.boid_pos = something
        return