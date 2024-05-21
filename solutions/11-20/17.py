one_digit = {
    "0" : 0,
    "1" : 3,
    "2" : 3,
    "3" : 5,
    "4" : 4,
    "5" : 4,
    "6" : 3,
    "7" : 5,
    "8" : 5,
    "9" : 4
}

ten_to_nineteen = { 
    "10" : 3,
    "11" : 6,
    "12" : 6,
    "13" : 8,
    "14" : 8,
    "15" : 7,
    "16" : 7,
    "17" : 9,
    "18" : 8,
    "19" : 8
}

twenty_to_ninety = {
    "2" : 6,
    "3" : 6,
    "4" : 5,
    "5" : 5,
    "6" : 5,
    "7" : 7,
    "8" : 6,
    "9" : 6
}

def single_digit(n):
    return one_digit[str(n)]

def double_digit(n):
    if 9 < n < 20:
        return ten_to_nineteen[str(n)]
    else:
        return twenty_to_ninety[str(n)[0]] + one_digit[str(n)[1]]

def triple_digit(n):
    if int(str(n)[1:]) == 0:
        return one_digit[str(n)[0]] + 7
    elif 0 < int(str(n)[1:]) < 10:
        return one_digit[str(n)[0]] + 10 + one_digit[str(n)[2]]
    elif 10 <= int(str(n)[1:]) < 20:
        return one_digit[str(n)[0]] + 10 + ten_to_nineteen[str(n)[1:]]
    else:
        return one_digit[str(n)[0]] + 10 + twenty_to_ninety[str(n)[1]] + one_digit[str(n)[2]]

sum = 0

for i in range(1, 10):
    sum += single_digit(i)

for i in range(10, 100):
    sum += double_digit(i)

for i in range(100, 1000):
    sum += triple_digit(i)

sum += 11

print(sum)