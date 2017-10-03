import P3  # imports 3-D vector class


class Boid:
    
    def __init__(self, flock, id, position, vel, acc = P3.P3(0, 0, 0)):
        
        self.id = id                # holding a unique identifying int
        self.position = position    # P3 holding the position or (x, y, z) of the boid
        self.vel = vel              # P3 holding the velosities of the boid
        self.acc = acc              # Float holding the acceleration
        self.flock = flock          # Current flock holding boid object 
    
    def move_Boid(self, tick): # Called to change the velocity and position of a particuliar boid
        
        self.vel = self.vel + self.acc * tick # Update velocity by adding the acceleration and multiplying by the tick
        
        self.position = self.position + self.vel * tick # Update position by adding the velocity and multiplying by the tick

