number = 1
i = 1

while i <= 20:
    if number % i != 0:
        number += 1
        i = 1    
    else:
        i += 1

print(number)