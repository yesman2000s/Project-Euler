import math
CurrentPrime = 0
Number = 600851475143

def CheckPrime(num):
    #check if prime

    check = False
    
    for x in range(3,num,1):
        if math.sqrt(num).is_integer():
            #print("is square")
            return False
        
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



for x in range(2,Number,1):
    if CheckPrime(x) == True:
        if (Number%x) == 0 and x > CurrentPrime:
            CurrentPrime = x
print(CurrentPrime)
#6857
