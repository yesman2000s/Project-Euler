from collections import deque
import time

def rotateNumber1(Number):
    CastedNumber = str(Number)
    numberList = []
    for x in CastedNumber:
        numberList.append(x)
    
    d = deque(numberList)
    allRotations = []

    for i in range(len(CastedNumber)):
        d.rotate()
        allRotations.append(d.copy())

    return allRotations


def rotation(N):
    output = []
    for i in range(len(N)):
        output.append(N[i:] + N[:i])
    return output

def Sieve(Limit):
    numbers = [True] * Limit
   
    numbers[0] = False
    numbers[1] = False
    for number,prime in enumerate(numbers):
         if prime:
             for j in range(number**2,Limit,number):
                 numbers[j] = False
    return numbers


primes = Sieve(1_000_000)
allPrimes = set()

for x in range(len(primes)):
    if primes[x]:
        allPrimes.add(x)

circularPrimes = []

def isCircularPrime(Number):
    allRotations = rotation(str(Number))
    allNumbers = [x for x in allRotations]
    

    for number in allRotations:
        if int(number) in allPrimes:
            continue
        else:
            return
    circularPrimes.append(x)

for x in range(1_000_000):
    isCircularPrime(x)

print(len(circularPrimes))