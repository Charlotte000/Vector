from math import sqrt, cos, sin, atan2, degrees, radians
from random import uniform

class Vector2:
    '''2D Vector'''
    DEGREES = False

    def __init__(self, x=0, y=0):
        if type(x) in [list, tuple]:
            if len(x) == 1:
                self.x = x[:]
                self.y = 0
            elif len(x) == 2:
                self.x, self.y = x[:]
        else:
            self.x = x
            self.y = y

    def setLength(self, length):
        '''Sets the vector length'''
        ve = self.copy()
        if ve.length() > 0:
            ve *= length / ve.length()
            self.x, self.y = ve.x, ve.y
        return self

    def length(self):
        '''Returns the vectors length'''
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def lengthSq(self):
        '''Returns the vectors length squared'''
        return pow(self.x, 2) + pow(self.y, 2)

    def angle(self):
        '''Return vectors angle between -pi and pi'''
        a = atan2(self.y, self.x)
        if Vector2.DEGREES:
            return degrees(a)
        return a

    def setAngle(self, angle):
        '''Sets the vector angle'''
        v = Vector2.fromAngle(angle)
        v *= self.length()
        self.x = v.x
        self.y = v.y
        return self

    def rotate(self, angle):
        '''Rotates the vector by Z axis by angle'''
        if Vector2.DEGREES:
            angle = radians(angle)
        x = self.x * cos(angle) - self.y * sin(angle)
        y = self.x * sin(angle) + self.y * cos(angle)

        self.x, self.y = x, y
        return self

    def copy(self):
        return Vector2(self.x, self.y)

    def constrain(self, minValue, maxValue):
        le = self.length()
        if le > maxValue:
            self.setLength(maxValue)
        elif le < minValue:
            self.setLength(minValue)
        return self

    @staticmethod
    def fromPoints(point1, point2):
        '''Returns the vector between point1 and point2'''
        return Vector2(*point2) - Vector2(*point1)

    @staticmethod
    def fromAngle(angle):
        '''Returns the unit vector with angle'''
        v = Vector2(1, 0)
        v.rotate(angle)
        return v

    @staticmethod
    def average(*vectors):
        '''Returns the mean vector'''
        v = Vector2()
        for vec in vectors:
            v += vec
        v /= len(vectors)
        return v

    @staticmethod
    def random():
        '''Returns a random unit vector'''
        a = Vector2(uniform(-1, 1), uniform(-1, 1))
        a.setLength(1)
        return a

    @staticmethod
    def angleBetween(v1, v2):
        a = atan2(v1.x * v2.y - v1.y * v2.x, v1.x * v2.x + v1.y * v2.y)
        if Vector2.DEGREES:
            return degrees(a)
        return a

    def __iadd__(self, vector):
        self.x += vector.x
        self.y += vector.y
        return self

    def __isub__(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        return self

    def __imul__(self, number):
        self.x *= number
        self.y *= number
        return self

    def __itruediv__(self, number):
        self.x /= number
        self.y /= number
        return self

    def __ifloordiv__(self, number):
        self.x //= number
        self.y //= number
        return self 

    def __add__(self, vector):
        v = self.copy()
        v += vector
        return v

    def __sub__(self, vector):
        v = self.copy()
        v -= vector
        return v

    def __mul__(self, number):
        v = self.copy()
        v *= number
        return v

    def __truediv__(self, number):
        v = self.copy()
        v /= number
        return v

    def __floordiv__(self, number):
        v = self.copy()
        v //= number
        return v

    def __str__(self):
        return f'Vector2[{self.x}, {self.y}]'

    def __getitem__(self, item):
        return [self.x, self.y][item]

    def __setitem__(self, item, value):
        if item == 0:
            self.x = value
        elif item == 1:
            self.y = value
        else:
            raise IndexError

    def __round__(self):
        return Vector2(round(self.x), round(self.y))

    def __iter__(self):
        return iter([self.x, self.y])

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __lt__(self, vector):
        return self.length() < vector.length()

    def __le__(self, vector):
        return self.length() <= vector.length()


class Vector3:
    '''3D Vector'''
    DEGREES = False

    def __init__(self, x=0, y=0, z=0):
        if type(x) in [list, tuple]:
            if len(x) == 1:
                self.x = x[:]
                self.y = self.z = 0
            elif len(x) == 2:
                self.x, self.y = x[:]
                self.z = 0
            elif len(x) == 3:
                self.x, self.y, self.z = x[:]
        else:
            self.x = x
            self.y = y
            self.z = z

    def setLength(self, length):
        '''Sets the vector length'''
        ve = self.copy()
        if ve.length() > 0:
            ve *= length / ve.length()
            self.x, self.y, self.z = ve.x, ve.y, ve.z
        return self

    def length(self):
        '''Returns the vectors length'''
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def lengthSq(self):
        '''Returns the vectors length squared'''
        return pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)

    def angle(self):
        '''Return vectors angle between -pi and pi on XY plane'''
        a = atan2(self.y, self.x)
        if Vector3.DEGREES:
            return degrees(a)
        return a

    def setAngle(self, angle):
        '''Sets the vector angle on XY plane'''
        v = Vector3.fromAngle(angle)
        v *= self.length()
        self.x = v.x
        self.y = v.y
        return self

    def rotate(self, angle):
        '''Rotates the vector by Z axis by angle'''
        if Vector3.DEGREES:
            angle = radians(angle)
        x = self.x * cos(angle) - self.y * sin(angle)
        y = self.x * sin(angle) + self.y * cos(angle)

        self.x, self.y = x, y
        return self

    def copy(self):
        return Vector3(self.x, self.y, self.z)

    def constrain(self, minValue, maxValue):
        le = self.length()
        if le > maxValue:
            self.setLength(maxValue)
        elif le < minValue:
            self.setLength(minValue)
        return self

    @staticmethod
    def fromPoints(point1, point2):
        '''Returns the vector between point1 and point2'''
        return Vector3(*point2) - Vector3(*point1)

    @staticmethod
    def fromAngle(angle):
        '''Returns the unit vector with angle. z coordinate is 0'''
        v = Vector3(1, 0, 0)
        v.rotate(angle)
        return v

    @staticmethod
    def average(*vectors):
        '''Returns the mean vector'''
        v = Vector3()
        for vec in vectors:
            v += vec
        v /= len(vectors)
        return v

    @staticmethod
    def random():
        '''Returns a random unit vector'''
        a = Vector3(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1))
        a.setLength(1)
        return a

    @staticmethod
    def angleBetween(v1, v2):
        a = atan2(v1.x * v2.y - v1.y * v2.x, v1.x * v2.x + v1.y * v2.y)
        if Vector3.DEGREES:
            return degrees(a)
        return a

    def __iadd__(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        return self

    def __isub__(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z
        return self

    def __imul__(self, number):
        self.x *= number
        self.y *= number
        self.z *= number
        return self

    def __itruediv__(self, number):
        self.x /= number
        self.y /= number
        self.z /= number
        return self

    def __ifloordiv__(self, number):
        self.x //= number
        self.y //= number
        self.z //= number
        return self

    def __add__(self, vector):
        v = self.copy()
        v += vector
        return v

    def __sub__(self, vector):
        v = self.copy()
        v -= vector
        return v

    def __mul__(self, number):
        v = self.copy()
        v *= number
        return v

    def __truediv__(self, number):
        v = self.copy()
        v /= number
        return v

    def __floordiv__(self, number):
        v = self.copy()
        v //= number
        return v

    def __str__(self):
        return f'Vector3[{self.x}, {self.y}, {self.z}]'

    def __getitem__(self, item):
        return [self.x, self.y, self.z][item]

    def __setitem__(self, item, value):
        if item == 0:
            self.x = value
        elif item == 1:
            self.y = value
        elif item == 2:
            self.z = value
        else:
            raise IndexError

    def __round__(self):
        return Vector3(round(self.x), round(self.y), round(self.z))

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False

    def __lt__(self, vector):
        return self.length() < vector.length()

    def __le__(self, vector):
        return self.length() <= vector.length()
