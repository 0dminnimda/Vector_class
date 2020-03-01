import numpy as np
from math import ceil, floor, sin, cos, pi, tau, atan2

class Vector:
    def __init__(se, e, s=None, n=2):
        #n = se.e.shape[0]
        se._n = n
        if type(s) == type(np.array([])):
            se.s = s
        elif s == None:
            se.s = np.zeros(n, dtype=np.float)
        else:
            se.s = np.array(s[:n], dtype=np.float)
        se.e = np.array(e[:n], dtype=np.float) + se.s
        se.ab = abs(se)
        
    def _st(se, a):
        return str(list(a))[1:-1]
        
    def __str__(se):
        return f"Vector{{{se._st(se.s)}}}{{{se._st(se.e-se.s)}}}"
        
    def __repr__(se):
        return se.__str__()
        
    def __add__(se, oth):
        e = se.ptsv()+oth.ptsv()#se.e+oth.e
        return Vector(e, se.s)
        
    def __sub__(se, oth):
        e = se.ptsv()-oth.ptsv()
        return Vector(e, se.s)
        
    def __mul__(se, oth):
        e = se.e*oth
        return Vector(e, se.s)
        
    def __truediv__(se, oth):
        e = se.e/oth
        return Vector(e, se.s)
        
    def __floordiv__(se, oth):
        e = se.e//oth
        return Vector(e, se.s)
        
    def __mod__(se, oth):
        e = se.e%oth
        return Vector(e, se.s)
        
    def __divmod__(se, oth):
        return se.__floordiv__(oth), se.__mod__(oth)
        
    def __round__(se):
        e = np.round(se.e)
        return Vector(e)
        
    def __ceil__(se):
        e = np.ceil(se.e)
        return Vector(e)
        
    def __floor__(se):
        e = np.floor(se.e)
        return Vector(e)
        
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
        return np.linalg.norm(se.e-se.s)
        
    def ang(se):
        return pi*12/16-atan2(*(se.e-se.s))
        
    def set_ang(se, alpha):
        rad = se.ab#abs(se)
        se.e[0] = se.s[0] + rad * cos(alpha)
        se.e[1] = se.s[1] + rad * sin(alpha)
        #return Vector(x, y)
        
    def turn(se, alp, pt):
        pass
        
    def link(se, oth):
        se.link = oth
        
    def set_abs(se, rad):
        #rad = se.ab
        se.e[0] = se.s[0] + rad * cos(se.ang())
        se.e[1] = se.s[1] + rad * sin(se.ang())
        
    def mul_abs(se, mul):
        ar = (se.s-se.e)*mul
        se.e = ar + se.s
        
    def perp(se, ar, ret=False):
        if ret is True:
            oth = se.copy()
        elif ret is False:
            oth = se
        for i in range(len(ar)):
            if 0 <= i <= oth._n:
                oth.e = oth.s+(oth.s-oth.ptsv())[::-1]
                if ar[i] == 0:
                    oth.e[0] = oth.s[0]-oth.ptsv()[0]
                elif ar[i] == 1:
                    oth.e[1] = oth.s[1]-oth.ptsv()[1]
                oth.e[i] = oth.s[i]-oth.ptsv()[i]
        if ret is True:
            return oth
            
    def copy(se):
        return Vector(se.ptsv(), se.s)
            
    def inv(se, *ar, ret=False):
        if ret is True:
            oth = se.copy()
            for i in ar:
                if 0 <= i <= oth._n:
                    oth.e[i] = oth.s[i]-oth.ptsv()[i]
            return oth
        if ret is False:
            for i in ar:
                if 0 <= i <= se._n:
                    se.e[i] = se.s[i]-se.ptsv()[i]
                    
    def draw(se, pd, r=1):
        pd.line(se.s, se.e, "red", r)
        #return (0, 0), (se.x, se.y)
        
    def pts(se):
        return se.s.copy(), se.e.copy()
        
    def ptsv(se):
        return (se.e-se.s).copy()
        
if __name__ == "__main__":
    v1 = Vector([3, 4], [0, 0, 0])
    v2 = Vector([12, 5], [4, 0])
    v3 = Vector([0.4, 0.5])
    num = 2
    print(v1, v2, v3, num)
    print(abs(v1), abs(v2))
    print(v1+v2)
    print(v1-v2, v2-v1)
    print(v1*num, v2*num)
    print(v1/num, v2/num)
    print(v1//num, v2//num)
    print(v1%num, v2%num)
    print(divmod(v1, num))
    print(divmod(v2, num))
    print(v1 < v2, v1 <= v2)
    print(v1 > v2, v1 >= v2)
    print(v1 == v2, v1 != v2)
    print(round(v3))
    print(ceil(v3))
    print(floor(v3))
    print(v2.pts(), v2.ptsv())