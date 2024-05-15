def palindrome_check(a):
    return a == a[::-1]

a = 999
b = 999

while True:
    if palindrome_check(str(a*b)):
        break
    a -= 1
    if palindrome_check(str(a*b)):
        break
    b-=1

print(a*b)
