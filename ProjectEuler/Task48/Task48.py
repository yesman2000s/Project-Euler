number = 0

for x in range(1,1001):
    number += x**x

print(str(number)[len(str(number)) - 10:])