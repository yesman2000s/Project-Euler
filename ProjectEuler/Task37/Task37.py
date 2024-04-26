def Sieve(Limit):
    numbers = [True] * Limit
   
    numbers[0] = False
    numbers[1] = False
    for number,prime in enumerate(numbers):
         if prime:
             for j in range(number**2,Limit,number):
                 numbers[j] = False
    return numbers


limit = 1_000_000

primes = Sieve(limit)
allPrimes = set()

for x in range(len(primes)):
    if primes[x]:
        allPrimes.add(x)


found = []

def isTruncatablePrime(prime):
    if prime not in allPrimes:
        return
    allTruncations = []
    prime = str(prime)
    for x in range(len(prime)):
        allTruncations.append(prime[:x])
    
    for x in range(len(prime)):
        allTruncations.append(prime[x:])

    for x in allTruncations:
        if len(str(x)) == 0:
            continue
        if int(x) in allPrimes:
            continue
        else:
            return
    
    found.append(int(prime))



for x in range(10,limit):
   isTruncatablePrime(x)

print(len(found))
print(sum(found))