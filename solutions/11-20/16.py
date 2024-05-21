n = 2

for i in range(2, 1001):
    n = n * 2

list = [int(digit) for digit in str(n)]

sum = sum(list[k] for k in range(len(list)))

print(sum)