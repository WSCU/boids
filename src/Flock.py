import Boid
import P3
import math
import random


class Flock:
    flock_count = 0
    
    def __init__(self, num_boids, center=P3.P3(0, 0, 0), radius=20): #possibly also orientation, maybe something about obstacles?
        Flock.flock_count += 1
        self.boids = []
        self.distance_matrix = [[0 for _ in range(num_boids)] for _ in range(num_boids)]

        # randomly distributes boids in circle on xy plane using center and radius
        for i in range(num_boids):
            r = radius * math.sqrt(random.random())
            theta = 2 * math.pi * random.random()
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            self.boids.append(Boid.Boid(self, i, P3.P3(x, y, 50) + center, P3.P3(-5, 0, 0), P3.P3(0, 0, 0)))

    def update(self, tick):
        for b in self.boids:
            b.move_Boid(self.distance_matrix, tick)
        self.update_dist_matrix()

    def update_dist_matrix(self):
        for i in range(len(self.boids)):
            for j in range(len(self.boids) - i - 1):
                self.distance_matrix[i][j] = self.boids[i].position.distance(self.boids[j].position)


if __name__ == '__main__':
    flock = Flock(10, P3.P3(100, 100, 1), 1)
    for b in flock.boids:
        print(b.position)