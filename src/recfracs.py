from math import trunc, e

def fraction(a = 1, n = 5, err = 10**-6):
    ints = [abs(trunc(a))]
    decs = [abs(a-trunc(a))]
    i = 0
    while not (-err < decs[-1] < err) and decs[-1] != 0 and i < n:
        u = 1/decs[i]
        ints.append(trunc(u))
        decs.append(u-trunc(u))
        i += 1
    v = round(decs[-1])
    n,d = 1 if v == 1 else 0,1
    for j in range(i + 1):
        v = round(decs[-j-1])
        u = ints[-j-1]
        n += u*d
        o = n
        n = d
        d = o
    if a < 0:
        d *= -1
    return d,n,d/n

def recfrac(a = 1, n = 5, err = 10**-6):
    pass

a = e

print (fraction(a,n=50))