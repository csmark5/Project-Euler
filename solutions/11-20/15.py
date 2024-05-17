from math import factorial as fact

def lattice(n):
    return fact(2 * n) / (fact(n) * fact(n))

print(lattice(20))
