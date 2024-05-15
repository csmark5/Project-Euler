from sympy import factorint

number = 600851475143

factors = factorint(number)

print(max(factors.keys()))