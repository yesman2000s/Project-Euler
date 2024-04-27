import itertools

perms = itertools.permutations('0123456789',10)

PRIMES = [2,3,5,7,11,13,17]


def check(x):
    if x[0] == '0':
        return False
    
    F = True
    for y in range(1,8):
        number = x[y]+x[y+1]+x[y+2]
        if int(number) % PRIMES[y-1] != 0:
            F = False
            break
    
    return F

SUM = 0

for x in perms:
    if check(x):
        number = ''
        for y in x:
            number += y

        SUM += int(number)    
print(SUM)