import math


class P3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __rmul__(self, scalar):
        return P3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self.__rmul__(other)
        return P3(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)

    def __add__(self, other):
        return P3(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return P3(self.x - other.x, self.y - other.y, self.z - other.z)

    def distance(self, other=None):  # returns magnitude if one argument is given
        other = other if other is not None else P3(0, 0, 0)
        return math.sqrt((self.x+other.x)**2 + (self.y+other.y)**2 + (self.z+other.z)**2)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        magnitude = self.distance() if self.distance() != 0 else 1
        return P3(self.x/magnitude, self.y/magnitude, self.z/magnitude)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    def to_dict(self):
        return dict(x=self.x,y=self.y,z=self.z)

    def from_dict(dict):
        return None if dict is None else P3(x=dict['x'], y=dict['y'], z=dict['z'])


if __name__ == "__main__":
    p1 = P3(1, 1, 1)
    p2 = P3(2, 5, 10)
    print(2 * p1)
    print(p1 * 2)
    print(p1 * p2)
    print(P3.normalize(p1))
    print(1.123 * p1)

    print()
    print(p2 - p1)
    p3 = P3(-100, 100, -100)
    print(p3 - p1)
