from math import sqrt, atan, pi, cos, sin, acos
from random import uniform


class Vector:
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
        if len(self.projection) < 2:
            if len(self.projection) == 1:
                ax, ay = self.projection[0], 0
            else:
                ax, ay = 0, 0
        else:
            ax, ay = self.projection[:2]

        if ax > 0:
            if ay > 0:
                return atan(ay / ax)
            elif ay < 0:
                return atan(ay / ax) + pi * 2
            else:
                return 0
        elif ax < 0:
            if ay > 0:
                return pi + atan(ay / ax)
            elif ay < 0:
                return pi + atan(ay / ax)
            else:
                return pi
        else:
            if ay > 0:
                return pi * .5
            elif ay < 0:
                return pi * 1.5
            else:
                return 0

    def round(self):
        return [round(i) for i in self.projection]

    def rotate2d(self, angle):
        if len(self.projection) < 2:
            self.projection.extend([0] * (2 - len(self.projection)))
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
        v11 = v1.copy()
        v22 = v2.copy()

        if len(v11.projection) == 1:
            v11.projection.append(0)
        if len(v22.projection) == 1:
            v22.projection.append(0)
        if v11.length() != 0 and v22.length() != 0:
            a = sum([v11[i] * v22[i] for i in range(2)]) / v11.length() / v22.length()
            return acos(round(a, 5))
        return 0


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
