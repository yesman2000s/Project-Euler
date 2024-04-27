import math
def createPentagonal(n):
    return n*((3*n) - 1) / 2



#checking if a number is pentagonal
# let x = a pentagonal number
# x = n(3n-1) / 2
# 2x = 3n^2 - n
# 0 = 3n^2 - n - 2x
#if n is whole (using quadratic formula) then x is pentagonal

def isPentagonal(x):
    a = 3
    b = -1
    c = -(2*x)
    discriminant = math.sqrt((
        (b**2) - (4*a*c)
    ))
    n1 = (-b + discriminant)/ 2*a
    n2 = (-b - discriminant)/ 2*a
    return n1.is_integer() or n2.is_integer()


pentagonals = [createPentagonal(x) for x in range(1,5000)]

possible = []

for x in pentagonals:
    for y in pentagonals:
        sum = x + y
        d1 = abs(x - y)
        if isPentagonal(sum) and isPentagonal(d1):
            possible.append(d1)


print(max(possible))

