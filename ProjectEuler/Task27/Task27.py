import math

def checkPrime(number):
    if number < 0:
        return False
    for num in range(2,math.floor(math.sqrt(number))+1):
        if number % num == 0:
            return False
    return True


#returns an array of all consec. primes in the given quadratic
def generateQuadratic(a,b):
    if checkPrime(b) == False:
        return 0
    n = 0
    while True: 
        solution = (a * n**2) + (b*n) + b
        n += 1
        if checkPrime(solution):
            continue
        else:
            break
    return n

longest = -1000
products = []

av = 0
ab = 0

for a in range(-1000,1000):
   for b in range(2,1001):
       products.append(generateQuadratic(a,b))

print(max(products))
