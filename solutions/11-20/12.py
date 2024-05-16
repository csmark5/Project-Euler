import math

def divisors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def triangle(n):
    return sum(k for k in range(1, n+1))

i = 0

while True:
    i += 1
    div = divisors(triangle(i))
    if div > 500:
        print(triangle(i))
        break
