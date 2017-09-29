import math


class P3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __rmul__(self, scalar):
        return P3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __mul__(self, other):
        return P3(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)

    def __add__(self, other):
        return P3(self.x+other.x, self.y+other.y, self.z+other.z)

    def distance(self, other=None):
        other = other if not None else P3(0, 0, 0)
        return math.sqrt((self.x+other.x)**2 + (self.y+other.y)**2 + (self.z+other.z)**2)

    def normalize(self):
        magnitude = self.distance()
        return P3(self.x/magnitude, self.y/magnitude, self.z/magnitude)
