fib = [1, 2]
sum = 2
index = 2

while True:
    index = len(fib)
    fib.append(fib[index-2]+fib[index-1])
    if fib[-1] > 4000000:
        break
    if fib[-1] % 2 == 0:
        sum += fib[-1]
    index += 1
    
print(sum)
