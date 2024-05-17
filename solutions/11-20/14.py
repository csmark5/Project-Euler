def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1
    
longest_chain = 0
start = 0

for i in range(2, 1000000):
    current = i
    chain = 1
    while current != 1:
        current = collatz(current)
        chain += 1
    if chain > longest_chain:
        longest_chain = chain
        start = i

print("longest chain: ", longest_chain, "\n", "start: ",start)