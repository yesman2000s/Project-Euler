#Cant be 1,2,3,5,6,8,9 digits long due to:
#1+2+3+4+5+6+7+8+9=45
#which is divisible by 3
#⇒
#any 9
#digit pandigital is divisible by 3
#True for cases 3,5,6,8,9 
#Case 1 only is 1.
#Case 2 only 2, 2 digit pandigital primes: 12, 21 - have factors
#Therefore must be 7 digits, brute force all primes upto 7 digits and find a pandigital.
#Can be made more efficient with having a lower limit.

def ispandigital(number):
    n = len(str(number))
    allowed = [str(x) for x in range(1,n+1)]

    return (allowed == sorted(str(number))) 


def Sieve(Limit):
    numbers = [True] * Limit
   
    numbers[0] = False
    numbers[1] = False
    for number,prime in enumerate(numbers):
         if prime:
             for j in range(number**2,Limit,number):
                 numbers[j] = False
                

    return numbers


LIMIT = 9999999
PRIMES = Sieve(LIMIT)

largest = 0 

for x in range(LIMIT):
    if ispandigital(x):
        IsPrime = PRIMES[x]
        if IsPrime:
            largest = x

print(largest)



