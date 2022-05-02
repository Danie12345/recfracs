import math

def recfracs(a = 1.0, n = None, p = None):
    if n == None:
        n = 0
        k = 10**(-p)
        escape = lambda r = None, k = None, n = None: 1 + k > abs(r) > 1 - k
        deepen = lambda r = None, k = None, n = None: not(1 + k > abs(r) > 1 - k)
    elif p == None:
        n = n
        k = 0
        escape = lambda r = None, k = None, n = None: n == 0
        deepen = lambda r = None, k = None, n = None: n > 0
    else:
        n = 8
        p = 4
        k = 10**(-p)
        escape = lambda r = None, k = None, n = None: n == 0 or 1 + k > abs(r) > 1 - k
        deepen = lambda r = None, k = None, n = None: n > 0 or not(1 + k > abs(r) > 1 - k)
    t = math.trunc(a)
    r = a - t
    R = 1/r
    if escape(r = r, k = k, n = n):
        n = 0
        r = 1
        return [1,1]
    elif deepen(r = r, k = k, n = n):
        y = recfracs(R, n = n - 1, p = p)
        y[0],y[1] = y[1],t*y[1]+y[0]
        return y