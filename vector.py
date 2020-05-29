from math import sqrt, cos, sin, acos, atan2, degrees, radians
from random import uniform


class Vector:
    AXES = ['x', 'y', 'z']
    DEGREES = False

    def __init__(self, *projection):
        if projection:
            self.projection = [i for i in projection]
        else:
            self.projection = []

    def add(self, *vectors):
        for vector in vectors:
            if len(self.projection) < len(vector.projection):
                self.projection.extend([0] * (len(vector.projection) - len(self.projection)))
            for i in range(len(vector.projection)):
                self.projection[i] += vector.projection[i]
        return self

    def remove(self, *vectors):
        for vector in vectors:
            vector2 = vector.copy()
            vector2.mult(-1)
            self.add(vector2)
        return self

    def mult(self, value):
        for i in range(len(self.projection)):
            self.projection[i] *= value
        return self

    def setLength(self, length):
        if self.length() > 0:
            self.mult(length / self.length())
            return self
        return self

    def length(self):
        return sqrt(sum([pow(d, 2) for d in self.projection]))

    def angle(self):
        a = atan2(self[1], self[0])
        if Vector.DEGREES:
            return degrees(a)
        return a

    def setAngle(self, angle):
        v = Vector.fromAngle(angle)
        v.mult(self.length())
        self.projection[0] = v.projection[0]
        self.projection[1] = v.projection[1]

    def round(self):
        return [round(i) for i in self.projection]

    def rotate2d(self, angle):
        if len(self.projection) < 2:
            self.projection.extend([0] * (2 - len(self.projection)))

        if Vector.DEGREES:
            angle = radians(angle)
        x = self.projection[0] * cos(angle) - self.projection[1] * sin(angle)
        y = self.projection[0] * sin(angle) + self.projection[1] * cos(angle)

        self.projection[0], self.projection[1] = x, y
        return self

    def copy(self):
        return Vector(*[i for i in self.projection])
    
    @staticmethod
    def fromPoints(point1, point2):
        v1 = Vector(*point1)
        v2 = Vector(*point2)
        v2.remove(v1)
        return v2

    @staticmethod
    def fromAngle(angle):
        v = Vector(1, 0)
        v.rotate2d(angle)
        return v
    
    @staticmethod
    def average(*vectors):
        v = Vector()
        v.add(*vectors)
        v.mult(1 / len(vectors))
        return v

    @staticmethod
    def random(dimension=2):
        a = Vector(*[uniform(-1, 1) for _ in range(dimension)])
        a.setLength(1)
        return a
    
    @staticmethod
    def angleBetween(v1, v2):
        a = atan2(v1.x * v2.y - v1.y * v2.x, v1.x * v2.x + v1.y * v2.y)
        if Vector.DEGREES:
            return degrees(a)
        return a

    def __add__(self, vector):
        if isinstance(vector, Vector):
            return self.copy().add(vector)

    def __sub__(self, vector):
        if isinstance(vector, Vector):
            return self.copy().remove(vector)

    def __mul__(self, number):
        if type(number) in [int, float]:
            return self.copy().mult(number)

    def __truediv__(self, number):
        if type(number) in [int, float]:
            return self.copy().mult(1 / number)

    def __round__(self):
        return self.round()

    def __str__(self):
        return 'Vector' + str(self.projection) + ""

    def __getitem__(self, item):
        if isinstance(item, int) and item >= len(self.projection):
            return 0
        return self.projection[item]

    def __setitem__(self, item, value):
        if isinstance(item, int):
            if len(self.projection) < item + 1:
                self.projection.extend([0] * (item + 1 - len(self.projection)))
            self.projection[item] = value
        else:
            i = [i for i in range(len(self.projection))]
            for j in i[item]:
                self.projection[j] = value

    def __getattr__(self, name):
        for i, n in enumerate(Vector.AXES):
            if n == name:
                return self[i]

    def __setattr__(self, name, value):
        for i, n in enumerate(Vector.AXES):
            if n == name:
                self[i] = value
                return
        return super().__setattr__(name, value)

    def __eq__(self, other):
        v1 = self.copy()
        v2 = other.copy()
        v2 *= -1
        if (v1 + v2).length() == 0:
            return True
        return False
