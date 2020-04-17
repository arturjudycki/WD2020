def wyraz_ciagu(a1,n,q):
    return a1 * (q ** (n-1))

def suma_ciagu(a1,n,q):
    if q == 1:
        return n * a1
    else:
        return a1 * (1 - (q ** n))/(1 - q)
