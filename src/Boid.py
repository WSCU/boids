import P3  # imports 3-D vector class
import Behavior

class Boid:
    
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, flock, id, position, vel, behavior):
        
        self.id = id                # holding a unique identifying int
        self.position = position    # P3 holding the position or (x, y, z) of the boid
        self.vel = vel              # P3 holding the velosities of the boid
        self.behavior = behavior             # Float holding the acceleration
=======
    def __init__(self, flock, id, position, velocity, behavior):
        
        self.id = id                # holding a unique identifying int
        self.position = position    # P3 holding the position or (x, y, z) of the boid
        self.velocity = velocity    # P3 holding the velosities of the boid
        self.behavior = behavior    # Float holding the behavior function
>>>>>>> master
=======
    def __init__(self, flock, id, position, velocity, behavior):
        
        self.id = id                # holding a unique identifying int
        self.position = position    # P3 holding the position or (x, y, z) of the boid
        self.velocity = velocity    # P3 holding the velosities of the boid
        self.behavior = behavior    # Float holding the behavior function
>>>>>>> master
        self.flock = flock          # Current flock holding boid object 
    
    def move_Boid(self, tick): # Called to change the velocity and position of a particuliar boid
        
<<<<<<< HEAD
<<<<<<< HEAD
        self.vel = self.vel + self.behavior(self) * tick # Update velocity by adding the acceleration and multiplying by the tick
        
        self.position = self.position + self.vel * tick # Update position by adding the velocity and multiplying by the tick

=======
        self.velocity = self.velocity + self.behavior(self) * tick # Update velocity by calling behavior function and multiplying by the tick
        
        self.position = self.position + self.velocity * tick # Update position by adding the velocity and multiplying by the tick
>>>>>>> master
=======
        self.velocity = self.velocity + self.behavior(self) * tick # Update velocity by calling behavior function and multiplying by the tick
        
        self.position = self.position + self.velocity * tick # Update position by adding the velocity and multiplying by the tick
>>>>>>> master
