primes = [2]

for a in range(3, 2000000):
    is_prime = True
    for prime in primes:
        if a % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(a)

print(sum(primes[-1]))