# Vector2 / Vector3

It is a simple Vector class in Python. Vector class provides 2/3 dimensional vectors and its converting.  
It also supports the use of mathematical expressions, such as +, -, /, *, //

---
_Vector2(x, y)_ - you can pass x, y or list.  
_Vector3(x, y, z)_ - you can pass x, y, z or list.
```python
v1 = Vector3(1, 2, 3)
v2 = Vector2(5, 6)
```
---
_Vector2.setLength(length)_ - sets the vector length to _length_
_Vector3.setLength(length)_ - same
```python
v1.setLength(1)
```
---
_Vector2.length()_ - return vectors length  
_Vector3.length()_ - same
```python
v1.length()
```
---
_Vector2.lengthSq()_ - return vectors length squared  
_Vector3.lengthSq()_ - same
```python
v1.lengthSq()
```
---
_Vector2.fromPoints(point1, point2)_ - returns the vector between point1 and point2  
_Vector3.fromPoints(point1, point2)_ - same, but _point_ containts 3 numbers
```python
Vector3.fromPoints([1, 2, 3], [4, 5, -5])
```
---
_Vector2.fromAngle(angle)_ - returns the unit vector with _angle_  
_Vector3.fromAngle(angle)_ - same, but _z_ coordinate is 0
```python
Vector2.fromAngle(pi / 2)
```
---
_Vector2.average(*vectors)_ - returns the mean vector  
_Vector3.average(*vectors)_ - same
```python
Vector2.average(v1, v2)
```
---
_Vector2.random()_ - returns a 2d random unit vector  
_Vector3.random()_ - same, but in 3 dimensions
```python
Vector2.random()
```
---
_Vector2.angle()_ - return vectors angle between -pi and pi on XY plane  
_Vector3.angle()_ - same
```python
v1.angle()
```
---
_Vector2.setAngle(angle)_ - sets the vector _angle_  
_Vector3.setAngle(angle)_ - same, but z coordinate doesn't change
```python
v1.setAngle(3.14)
```
---
_Vector2.angleBetween(v1, v2)_ - returns the angle between v1 and v2 on XY plane between -pi and pi  
_Vector3.angleBetween(v1, v2)_ - same
```python
Vector2.angleBetween(v1, v2)
```
---
_Vector2.rotate(angle)_ - rotates the vector by Z axis by _angle_  
_Vector3.rotate(angle)_ - same
```python
v1.rotate(pi)
```
---
_Vector2.copy()_ - returns the copy of the vector  
_Vector3.copy()_ - same
```python
v1.copy()
```
---
_Vector2.constrain(minValue, maxValue)_ - constraints vector's length between _minValue_ and _maxValue_  
_Vector3.constrain(minValue, maxValue)_ - same
```python
v1.constrain(1, 2)
```
---
_Vector2.DEGREES_ - bool variable that enables working with degrees. False by default  
_Vector3.DEGREES_ - same
```python
Vector2.DEGREES = True
```