import P3 # imports 3-D vector class

class Boid:
    
    def __init__(self, flock, id, position, velocity, behavior):
        
        self.id = id                # holding a unique identifying int
        self.position = position    # P3 holding the position or (x, y, z) of the boid
        self.velocity = velocity    # P3 holding the velosities of the boid
        self.behavior = behavior    # Float holding the behavior function
        self.flock = flock          # Current flock holding boid object 
    
    def move_Boid(self, tick): # Called to change the velocity and position of a particuliar boid
        
        self.velocity = self.velocity + self.behavior(self) * tick # Update velocity by calling behavior function and multiplying by the tick
        
        self.position = self.position + self.velocity * tick # Update position by adding the velocity and multiplying by the tick
