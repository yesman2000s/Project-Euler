import math


def checkPrime(number):
    if number <0:
        return False
    for num in range(2, math.isqrt(number) + 1):
        if number % num == 0:
            return False
    return True

# returns an array of all consecutive primes in the given quadratic
def generateQuadratic(a, b):
    if not checkPrime(b):
        return 0
    n = 0
    while True:
        solution = ((n ** 2)) + (a * n) + b
        if checkPrime(solution):
            n += 1
        else:
            break
    return n


longestChainLength = 0
product = 0

for a in range(-999, 1000):
    for b in range(2, 1001):  # b must be a prime number
        if not checkPrime(b):
            continue
        solution = generateQuadratic(a,b)
        if solution > longestChainLength:
            longestChainLength = solution
            product = a*b

print(longestChainLength , product)


