def palindrome_check(a):
    return a == a[::-1]

max = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if palindrome_check(str(i * j)) and max < i * j:
            max = i * j

print(max)
