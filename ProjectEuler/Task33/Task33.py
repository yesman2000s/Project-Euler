import math

def replacedigit(digit:str, replace:str):
    new = ''
    for x in digit:
        if x != replace:
            new += x
    return new

allDenominators = []
allNumerators = []

def simplify(numerator,denominator):
    d = math.gcd(numerator, denominator);
    
    numerator = numerator // d;
    denominator = denominator // d;

    return numerator,denominator

def iscuriousfraction(numerator,denominator):
    #find digit which is in both?
    
    originaln = numerator
    originald = denominator

    if numerator%10 == 0 and denominator%10 == 0:
        return
    if numerator%11 == 0 or denominator%11 == 0:
        return
    digitsInBoth = set()
    for x in str(numerator):
        if x in str(denominator):
            digitsInBoth.add(x)
    
    if len(digitsInBoth) == 2:
        return 
    
    for x in digitsInBoth:
        #remove the digit from both numbers

        if x == 0:
            return 
        numerator = str(numerator)
        denominator = str(denominator)


        numerator = replacedigit(numerator,str(x))
        denominator = replacedigit(denominator,str(x))

        #print(f"After removing duplications the fraction is {numerator}/{denominator}")

        if int(denominator) <1:
            return

        if (int(numerator)/int(denominator)) < 1:
            if numerator == '0':
                return
            
            simplifiedn,simplifiedd = simplify(int(numerator),int(denominator))

            if simplifiedn/simplifiedd == originaln/originald:
                allNumerators.append(int(numerator))
                allDenominators.append(int(denominator))


for a in range(10,100,1):
    for b in range(10,100,1):
        iscuriousfraction(a,b)

productOfNumerators = 1
productOfDenominators = 1

for x in range(len(allNumerators)):
    productOfNumerators *= allNumerators[x]
    productOfDenominators *= allDenominators[x]

_, d = simplify(productOfNumerators,productOfDenominators)

print(d)