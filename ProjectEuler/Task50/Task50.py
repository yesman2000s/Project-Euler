def Sieve(Limit):
    numbers = [True] * Limit
   
    numbers[0] = False
    numbers[1] = False
    for number,prime in enumerate(numbers):
         if prime:
             for j in range(number**2,Limit,number):
                 numbers[j] = False
    return numbers

LIMIT = 1_000_000
PRIMES = Sieve(LIMIT)
PRIME_NUMBERS = [x for x in range(LIMIT) if PRIMES[x]]

#Start with all the prime numbers that make a sum that is less than the said limit

NEW_PRIMES = []

for y in PRIME_NUMBERS:
    if sum(NEW_PRIMES) + y < LIMIT:
        NEW_PRIMES.append(y)

while not PRIMES[sum(NEW_PRIMES)]:
    NEW_PRIMES.pop(0)

print(sum(NEW_PRIMES))