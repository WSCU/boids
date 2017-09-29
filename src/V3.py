# Simple 3-D vector class

class V3:
    
    x = 0
    y = 0
    z = 0
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "x = {}, y = {}, z = {}".format(self.x, self.y, self.z)
       
    # Override mul to Scalar Multiplication    
    def __mul__(self, number):
        return V3(self.x * number, self.y * number, self.z * number)
    
    # Override add to Vector Addition
    def __add__(self, v3Added):
        return V3(self.x + v3Added.x, self.y + v3Added.y, self.z + v3Added.z)


# test __add__ and __mul__
if __name__ == "__main__":
    
    a = V3(1,2,3)
    b = V3(1,2,3)
    
    c = a + b # using __add__
    print(c)
    
    c = a * 2 #using __mul__
    print(c)
        


