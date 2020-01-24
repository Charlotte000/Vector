from math import sqrt, atan, pi


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
            vector2 = Vector.get_copy(vector)
            vector2.multiply(-1)
            self.add(vector2)
        return self

    def mult(self, value):
        for i in range(len(self.projection)):
            self.projection[i] *= value
        return self

    def setLength(self, length):
        self.multiply(length / self.length())
        return self

    def length(self):
        return sqrt(sum([pow(d, 2) for d in self.projection]))

    def angle(self):
        ax, ay = self.projection
        if ax:
            return atan(ay / ax) + pi / 2
        if ay > 0:
            return pi / 2
        if ay < 0:
            return -pi / 2
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
    
    def __str__(self):
        return 'Vector' + str(self.projection) + ""

    def __getitem__(self, item):
        if item >= len(self.projection):
            return 0
        return self.projection[item]
    

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
        v.multiply(1 / len(vectors))
        return v
