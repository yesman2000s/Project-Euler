import itertools

def Sieve(Limit):
    numbers = [True] * Limit
   
    numbers[0] = False
    numbers[1] = False
    for number,prime in enumerate(numbers):
         if prime:
             for j in range(number**2,Limit,number):
                 numbers[j] = False
                

    return numbers

PRIMES = Sieve(20000)



def sequence_gen(n,perms):
    seq_bool=False
    seq=[]
    fin =[]
    for q in perms:
        if (q+(q-n)) in perms:
            seq =[n,q,2*q-n]
            seq_bool=True
    return seq_bool , seq
for x in range(1000,10001):
    if PRIMES[x]:
        pass
        #get all permutations of this number.
        #if the permutations are prime and greater we found it! 
        perms = itertools.permutations(str(x))
        pool = [] # all the number permutations of x
        for y in perms:
            number = ''
            for num in y:
                number += num
            if PRIMES[int(number)] and int(number) != x and len(number) >3:
                pool.append(int(number))
        
        pool = set(pool)
        
        t, seq = sequence_gen(x,pool)
        if t and seq:
            s = ''
            for x in seq:
                s += str(x)
            print(f'Solution {s} with length {len(s)}')
