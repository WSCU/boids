import P3  # imports 3-D vector class
import Behavior

class Boid:
    
    def __init__(self, flock, id, position, vel, behavior):
        
        self.id = id                # holding a unique identifying int
        self.position = position    # P3 holding the position or (x, y, z) of the boid
        self.vel = vel              # P3 holding the velosities of the boid
        self.behavior = behavior             # Float holding the acceleration
        self.flock = flock          # Current flock holding boid object 
    
    def move_Boid(self, tick): # Called to change the velocity and position of a particuliar boid
        
        self.vel = self.vel + self.behavior(self) * tick # Update velocity by adding the acceleration and multiplying by the tick
        
        self.position = self.position + self.vel * tick # Update position by adding the velocity and multiplying by the tick

