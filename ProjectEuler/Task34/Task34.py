import math

def isCurious(digit):
    temp = str(digit)
    
    sumOfFactorials = 0

    for x in temp:
        sumOfFactorials += math.factorial(int(x))
    
    return sumOfFactorials == digit

total = 0

for x in range(3,1499999):
    if isCurious(x):
        total += x

print(total)
