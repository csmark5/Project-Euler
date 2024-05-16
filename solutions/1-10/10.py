#Sieve of Eratosthenes algorithm

primes = [True] * (2000001)
primes[0] = False
primes[1] = False

n = 2
while n * n <= 2000000:
    if primes[n]:
        for i in range(n * n, 2000001, n):
            primes[i] = False
    n += 1

all_primes = [i for i in range(2, 2000001) if primes[i]]

print(sum(all_primes))