import math

##
##def Sieve(Limit):
##    numbers = [True] * Limit
##   
##    numbers[0] = False
##    numbers[1] = False
##    for number,prime in enumerate(numbers):
##         if prime:
##             for j in range(number**2,Limit,number):
##                 numbers[j] = False
##                
##                
##
##    return enumerate(numbers)

def divisors(num):
    #get number of divisors of a given integer and return it
    numdiv = 0
    sqrt = math.floor(math.sqrt(num))
    for x in range(1 , int(sqrt+1)):
        if num%x == 0:
            numdiv += 2
    if sqrt ** 2 == num:
        numdiv -= 1

    return numdiv


def getTriangle(num):
    # num is an integer, is the  triangle we  want to get
    #7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
    trinum = 0
    for x in range(1,num+1):
        trinum += x

    return trinum
##
TriNumFound = False
TriNum =0
TriValue = 0
Max = 500


while not TriNumFound:
    TriNum += 1
    num = getTriangle(TriNum)
    divs = divisors(num)
   # print(f"{TriNum} has {divs}")
    if divs > Max:
        TriNumFound = True
        TriValue = num
        break

print(f"The triangle number in sequence is {TriNum} , the value is {TriValue} it has {Max} divisors")




