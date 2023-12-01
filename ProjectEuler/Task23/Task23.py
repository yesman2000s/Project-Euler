#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#A perfect number is a number whose divisors sum to the number.
#An abundant number is where the divisors sum to 
#All numbers > 28123 can be written as the sum of two abundant numbers
#Find the sum of all positive integers which cannot be written as the sum of two abundant numbers

import math


MAX = 28123
abundantNumbers = []

def getDivisors(number):
    divisors = []
    for x in range(1,round(math.sqrt(number)+1)):
        if number % x == 0:
            divisors.append(x)
            matchingPair = round(number/x)
            if x!= matchingPair:
                divisors.append(matchingPair)
    
    divisors.remove(number)
    return divisors

for x in range(12,MAX):
    sumOfDivisors = sum(getDivisors(x))
    if sumOfDivisors > x:
        abundantNumbers.append(x)

allPossibleNumbers = [False] * (MAX+1)

for x in range(len(abundantNumbers)):
    for y in range(len(abundantNumbers)):
        sumOfTwoAbundantNumbers = abundantNumbers[x] + abundantNumbers[y]
        if (sumOfTwoAbundantNumbers) > (MAX):
            continue
        else:
            allPossibleNumbers[sumOfTwoAbundantNumbers] = True

total = 0

for x in range(len(allPossibleNumbers)):
    if allPossibleNumbers[x] == False:
        total += x

print(total)