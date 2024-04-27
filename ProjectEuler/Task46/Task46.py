#An odd number which is not prime

# k = p + 2i^2
# i = k-p / 2 
#where p is a prime
#use sieve to generate primes

#find where i is not an integer
import math

def isSquare(n):
    return math.sqrt(n).is_integer()

def Sieve(Limit):
    numbers = [True] * Limit
   
    numbers[0] = False
    numbers[1] = False
    for number,prime in enumerate(numbers):
         if prime:
             for j in range(number**2,Limit,number):
                 numbers[j] = False
                

    return numbers


LIMIT = 10_000
PRIMES = Sieve(LIMIT)

def composite(x):
    if PRIMES[x]:
        return False
    if x == 1:
        return False
    
    possiblePrimes = [y for y in range(len(PRIMES)) if y<=x and PRIMES[y] == True]
    matching = 0
    for z in possiblePrimes:
        if isSquare((x-z)/2):
            matching += 1

    return matching == 0

for x in range(1,LIMIT,2):
    if composite(x):
        print(x)

