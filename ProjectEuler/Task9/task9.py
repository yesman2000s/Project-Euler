#find triplets
#check if a + b + c = 1000
# a<b<c<1000

import math

for a in range(1,1001): #has to be less than 1000
    for b in range(a+1,1001): #b must be greater than  a -> a+1
        #get c
        c = a*a + b*b
        c = math.sqrt(c)
        if a + b + c == 1000:
            print(a*b*c)
#31875000.0
        
            
