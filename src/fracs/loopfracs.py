import math
from decimal import Decimal

def nEscape(n, i = 0):
    return i > n

def kEscape(r, k, a):
    return k > abs(r - Decimal(a)) > -k

def build_frac(ints, decs, a, v=1):
    v = round(decs[-1])
    n,d = 1 if v == 1 else 0,1
    for j in range(len(decs) + 1):
        u = ints[-j]
        n += u*d
        n,d=d,n
    if a < 0:
        d *= -1
    return d,n,Decimal(d)/Decimal(n)

def loopfracs(a = 1.0, n = None, p = None):
    if n == None and p != None:
        k = 10**(-p)
        escape = lambda r = None,  n = None, i = None: kEscape(r, k, a)
    elif n != None and p == None:
        k = 10**-14
        escape = lambda r = None,  n = None, i = None: nEscape(n, i)
    else:
        n = n if n != None else 10
        p = p if p != None else 16
        k = 10**(-p)
        escape = lambda r = None,  n = None, i = None: nEscape(n, i) or kEscape(r, k, a)
    ints = [abs(math.trunc(a))]
    decs = [abs(a-math.trunc(a))]
    i = 0
    r = 10**100
    # while not (kEscape(decs[-1], k)) and decs[-1] != 0 and escape(r = r, n = n, i = i):
    while not escape(r, n, i):
        u = 1/decs[i]
        ints.append(math.trunc(u))
        decs.append(u-math.trunc(u))
        r = build_frac(ints, decs, a)[2]
        if abs(Decimal(a) - Decimal(r)) < k:
            print('breaking from r',abs(Decimal(a) - Decimal(r)), a, r, k)
            break
        i += 1
    return build_frac(ints,decs,a,v=round(decs[-1]))

if __name__ == '__main__':
    a = 1.1
    b = loopfracs(a, n=3, p = 10)
    print (b)