import math

def getDivisors(number):
    divisors = []
    for x in range(1,round(number/2)+1):
        if number % x == 0:
            divisors.append(x)
    return divisors

def amicable(number):
    return sum(getDivisors(number))

amicableNumbers = []


for x in range(1,10001):
    a = amicable(x)
    b = amicable(a)
    if x == b and x != a:
        amicableNumbers.append(x)


print(sum(amicableNumbers))