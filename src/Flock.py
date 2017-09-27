import Boid


class Flock:
    flockcount = 0

    def __init__(self, num_boids, center, radius): #possibly also orientation, maybe something about obstacles?
        self.num_boids = num_boids
        self.center = center
        self.radius = radius
        self.boid_list = []
        self.flockcount += 1
        self.distance_matrix = [[0 for _ in range(num_boids)] for _ in range(num_boids)]

        row = -1
        for i in range(num_boids):
            if i % 10 == 0:
                row += 1
            self.boid_list.append(Boid(i, (200 - 10*row, -20 + 4*i, 50), (-22, 0, 0), 0)) #if velocity and position are tuples

    def update(self):
        return self.boid_list

    def dist_matrix(self):
        for i in range(len(self.boid_list)):
            for j in range(len(self.boid_list)-i):
                self.distance_matrix[i][j] = Boid.distance(self.boid_list[i], self.boid_list[j]) #using Boid.distance method
