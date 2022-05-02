import math

def rec(s, n=12, p=8):
    k = 10**(-p)
    n -= 1
    t = math.trunc(s)
    r = s - t
    R = 1/r
    if n == 0 or 1 + k > abs(r) > 1 - k:
        n = 0
        r = 1
        return [1,1]
    elif n > 0:
        y = rec(R, n=n, p=p)
        y[0],y[1] = y[1],t*y[1]+y[0]
        return y