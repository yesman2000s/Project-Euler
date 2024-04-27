primeFactors = {}

def primeFactor(number):
    start = number

    if start in primeFactors:
        return primeFactors[start]

    if number == 1:
        return [1]
    n = 2
    factors = []
    while n ** 2 <= number: #prime factor cant be larger than the square root 
        if number % n == 0:
            factors.append(n)
            number //= n
        else:
            n += 1
    if number > 1:
        factors.append(number)

    primeFactors[start] = factors

    return factors



for x in range(500000):
    if len(set(primeFactor(x))) == 4:
        if len(set(primeFactor(x+1))) == 4:
            if len(set(primeFactor(x+2))) == 4:
                if len(set(primeFactor(x+3))) == 4:
                    print(x)
                    break

