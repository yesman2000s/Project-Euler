import math

def CheckPrime(num):
    #check if prime

    check = False
    
    for x in range(0,num,1):
        
        if math.sqrt(num).is_integer():
            #print("is square")
            return False
        if x == 0:
            continue
        if x > 1:
            if (num%x) == 0:
               # print(f"{num} over {x} is a whole number")
                check = False
                break
            
            elif (num%x) != 0:
               # print(f"When {num} over {x}, not w. number")
                #number is prime
                check = True
                continue

    
    if check == True:
        return check
    else:
        return check


PrimesFound = 0
Number = -1
PrimeToFind = 10000

while PrimesFound <= PrimeToFind:
    Number += 1
    
    IsPrime = CheckPrime(Number)
    if IsPrime:
        PrimesFound += 1
       
        if PrimesFound >= PrimeToFind:
            break
    else:
        continue

print(Number)
#104743
