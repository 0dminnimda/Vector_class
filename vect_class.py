import numpy as np
from math import ceil, floor

class Vector:
    def __init__(se, x=0, y=0):
        se.x = x
        se.y = y
        
    def __str__(se):
        return f"Vector{{{se.x}; {se.y}}}"
        
    def __repr__(se):
        return f"Vector{{{se.x}; {se.y}}}"
        
    def __add__(se, oth):
        x = se.x + oth.x
        y = se.y + oth.y
        return Vector(x, y)
        
    def __sub__(se, oth):
        x = se.x - oth.x
        y = se.y - oth.y
        return Vector(x, y)
        
    def __mul__(se, oth):
        x = se.x * oth
        y = se.y * oth
        return Vector(x, y)
        
    def __truediv__(se, oth):
        x = se.x / oth
        y = se.y / oth
        return Vector(x, y)
        
    def __floordiv__(se, oth):
        x = se.x // oth
        y = se.y // oth
        return Vector(x, y)
        
    def __mod__(se, oth):
        x = se.x % oth
        y = se.y % oth
        return Vector(x, y)
        
    def __divmod__(se, oth):
        return se.__floordiv__(oth), se.__mod__(oth)
        
    def __round__(se):
        x = round(se.x)
        y = round(se.y)
        return Vector(x, y)
        
    def __ceil__(se):
        x = ceil(se.x)
        y = ceil(se.y)
        return Vector(x, y)
        
    def __floor__(se):
        x = floor(se.x)
        y = floor(se.y)
        return Vector(x, y)
        
    def __lt__(se, oth):
        return abs(se) < abs(oth)
        
    def __le__(se, oth):
        return abs(se) <= abs(oth)
        
    def __eq__(se, oth):
        return abs(se) == abs(oth)
        
    def __ne__(se, oth):
        return abs(se) != abs(oth)
        
    def __gt__(se, oth):
        return abs(se) > abs(oth)
        
    def __ge__(se, oth):
        return abs(se) >= abs(oth)
        
    def __abs__(se):
        return np.linalg.norm([se.x, se.y])
        
v1 = Vector(1, 5)
v2 = Vector(12, 5)
v3 = Vector(0.4, 0.5)
num = 2
print(v1, v2, v3, num)
print(abs(v1), abs(v2))
print(v1+v2)
print(v1-v2, v2-v1)
print(v1*num, v2*num)
print(v1/num, v2/num)
print(v1//num, v2//num)
print(v1%num, v2%num)
print(divmod(v1, num), divmod(v2, num))
print(v1 < v2, v1 <= v2)
print(v1 > v2, v1 >= v2)
print(v1 == v2, v1 != v2)
print(round(v3))
print(ceil(v3))
print(floor(v3))