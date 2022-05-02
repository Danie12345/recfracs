import math

def recfracs(a = 1, n=12, p=8):
    k = 10**(-p)
    n -= 1
    t = math.trunc(a)
    r = a - t
    R = 1/r
    if n == 0 or 1 + k > abs(r) > 1 - k:
        n = 0
        r = 1
        return [1,1]
    elif n > 0:
        y = recfracs(R, n=n, p=p)
        y[0],y[1] = y[1],t*y[1]+y[0]
        return y