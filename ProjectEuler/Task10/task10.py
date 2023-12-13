def Sieve(Limit):
    numbers = [True] * Limit
   
    numbers[0] = False
    numbers[1] = False
    for number,prime in enumerate(numbers):
         if prime:
             for j in range(number**2,Limit,number):
                 numbers[j] = False
                
                

    return enumerate(numbers)


total = 0

sieved = Sieve(2000000)

for y,z in sieved:
    if z:
        total += y

print(total)
#142913828922
