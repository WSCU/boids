import Boid
import P3


class Flock:
    flockcount = 0
    
    def __init__(self, num_boids, center, radius): #possibly also orientation, maybe something about obstacles?
        self.num_boids = num_boids
        self.boids = []
        #Flock.flock_count += 1
        self.distance_matrix = [[0 for _ in range(num_boids)] for _ in range(num_boids)]

        # defaults boid to grid
        row = -1
        for i in range(num_boids):
            if i % 10 == 0:
                row += 1
            self.boids.append(Boid.Boid(i, P3.P3(200 + 10 * row, -20 + 4 * i, 50), P3.P3(-15, 0, 0), P3.P3(0, 0, 0), self))
            # self.boids.append(Boid.Boid(i, P3.P3(0 + 10 * row, i, 20 - 4 * i), P3.P3(-5, 0, 0), P3.P3(0, 0, 0), self))


    def update(self, tick):
        for b in self.boids:
            b.self.move_Boid(self.distance_matrix, tick)
        self.dist_matrix()

    def dist_matrix(self):
        for i in range(len(self.boids)):
            for j in range(len(self.boids) - i-1):
                self.distance_matrix[i][j] = self.boids[i].position.distance(self.boids[j].position)
