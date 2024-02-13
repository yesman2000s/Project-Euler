import math

panDigitals = []



def isPandigital(digit:str):
    return sorted(digit) == list('123456789')

def deconstruct(digit:int):
    #get all factors
    factors = []
    for x in range(1,int(math.sqrt(digit) + 1)):
        if digit%x == 0:
            factors.append(x)
    
    #go through the factors.
    
    for factor in factors:
        multiplancd = digit // factor
        alldigits = str(multiplancd) + str(factor) + str(digit)

        if isPandigital(alldigits):
            panDigitals.append(digit)
            break


for x in range(100_000):
    deconstruct(x)

print(sum(panDigitals))


