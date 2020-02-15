# Vector

It is s a simple Vector class in Python. Vector class provides multi dimensional vectors and its converting. 

---
_Vector(*projection)_ - you can pass as many dimension vector as you want.
```python
v1 = Vector(1, 2, 3, 4)
v2 = Vector(5, 6)
```
---
_Vector.add(*vectors)_ - adds all _vectors_ to v1
```python
v1.add(v2)
```
---
_Vector.remove(*vectors)_ - subtracts all _vectors_ from v1
```python
v1.remove(v2)
```
---
_Vector.mult(value)_ - multiplies v1 by _number_
```python
v1.mult(5)
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
_Vector.rotate2d(angle)_ - rotates the vector by Z axis by _angle_ in radians
```python
v1.rotate2D(3.14)
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
_Vector.random(dimension)_ - returns the random unit vector of _dimension_
```python
Vector.random(3)
```
