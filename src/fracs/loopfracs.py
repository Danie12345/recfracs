import math

def loopfracs(a = 1.0, n = 5, err = 10**-4):
    ints = [abs(math.trunc(a))]
    decs = [abs(a-math.trunc(a))]
    i = 0
    while not (-err < decs[-1] < err) and decs[-1] != 0 and i < n:
        u = 1/decs[i]
        ints.append(math.trunc(u))
        decs.append(u-math.trunc(u))
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