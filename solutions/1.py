sum = 0

for number in range(1, 1001):
    if number % 3 == 0:
        if number % 5 == 0:
            sum += number

print(sum)