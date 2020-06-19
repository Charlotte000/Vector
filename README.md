# Vector

It is a simple Vector class in Python. Vector class provides max 3 dimensional vectors and its converting.  
It also supports the use of mathematical expressions, such as +, -, /, *

---
_Vector(x, y, z)_ - you can pass x, y, z or list.
```python
v1 = Vector(1, 2, 3)
v2 = Vector(5, 6)
```
---
_Vector.setLength(length)_ - sets the vector length to _length_
```python
v1.setLength(1)
```
---
_Vector.length()_ - returns the vector length
```python
v1.length()
```
---
_Vector.round()_ - returns the rounded projection of the vector as a tuple
```python
v1.round()
```
---
_Vector.fromPoints(point1, point2)_ - returns the vector between point1 and point2
```python
Vector.fromPoints([1, 2, 3], [4, 5])
```
---
_Vector.fromAngle(angle)_ - returns the unit vector with _angle_
```python
Vector.fromAngle(pi / 2)
```
---
_Vector.average(*vectors)_ - returns the mean vector
```python
Vector.average(v1, v2)
```
---
_Vector.random2D()_ - returns a 2d random unit vector
```python
Vector.random2D()
```
---
_Vector.random3D()_ - returns a 3d random unit vector
```python
Vector.random3D()
```
---
_Vector.angle()_ - returns the vector angle between -pi and pi on XY plane
```python
v1.angle()
```
---
_Vector.setAngle(angle)_ - sets the vector _angle_
```python
v1.setAngle(3.14)
```
---
_Vector.angleBetween(v1, v2)_ - returns the angle between v1 and v2 on XY plane between -pi and pi
```python
Vector.angleBetween(v1, v2)
```
---
_Vector.rotate2d(angle)_ - rotates the vector by Z axis by _angle_ in radians
```python
v1.rotate2D(pi)
```
---
_Vector.copy()_ - returns the copy of the vector
```python
v1.copy()
```
---
_Vector.constrain(minValue, maxValue)_ - constraints vector's length between _minValue_ and _maxValue_
```python
v1.constrain(1, 2)
```
---
_Vector.DEGREES_ - bool variable that enables working with degrees. False by default
```python
Vector.DEGREES = True
```