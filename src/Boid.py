import P3 # imports 3-D vector class

class Boid:
    
    def __init__(self, id, position, vel, acc = 0, flock):
        
        self.id = id                # holding a unique identifying int
        self.position = position    # P3 holding the position or (x, y, z) of the boid
        self.vel = vel              # P3 holding the velosities of the boid
        self.acc = acc              # Float holding the acceleration
        self.flock = flock          # Current flock holding boid object 
    
    def move_Boid(self, tick): # Called to change the velocity and position of a particuliar boid
        
        rule1V = rule1(self)  # Calculate rule's v3 from behaviors import
        rule2V = rule2(self)
        rule3V = rule3(self)
        
        self.vel = self.vel + rule1V + rule2V + rule3V # Add each rule's v3 to the boid's velocity
        
        self.position += self.vel # Update position by adding the newly created velocity to the original position
        
        
        
        
        
        
        
        
        
    
        
        
    
    

    