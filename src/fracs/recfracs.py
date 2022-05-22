from __future__ import nested_scopes
import math

def nEscape(n):
    return n <= 0

def kEscape(r, k):
    return k > abs(r) > -k

def recfracs(a = 1.0, n = None, p = None):
    t = math.trunc(a)
    r = a - t
    try:
        R = 1/r
    except:
        R = 0
    if n == None and p != None:
        n = None
        k = 10**(-p)
        escape = lambda: kEscape(r, k)
        deepen = lambda: not(kEscape(r, k))
    elif n != None and p == None:
        n = n
        p = None
        escape = lambda: nEscape(n)
        deepen = lambda: not(nEscape(n))
    else:
        n = n if n != None else 10
        p = p if p != None else 16
        k = 10**(-p)
        escape = lambda: nEscape(n) or kEscape(r, k)
        deepen = lambda: not(nEscape(n)) or not(kEscape(r, k))
    if escape():
        return [0,1]
    elif deepen():
        l = n if n != None else 0
        y = recfracs(a = R, n = l - 1, p = p)
        y[0],y[1] = y[1], t * y[1] + y[0]
        print (y)
        return y

if __name__ == '__main__':
    a = 1.4
    b = recfracs(a, n = 4, p = 4)
    print (b)