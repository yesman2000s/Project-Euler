import math

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

#let x be a trianglar number
# 2x = n^2 + n
# 0 = n^2 + n - 2x

def isTriangle(x):
    a = 1
    b = 1
    c = -(2*x)
    discriminant = math.sqrt((
        (b**2) - (4*a*c)
    ))
    n1 = (-b + discriminant)/ 2*a
    n2 = (-b - discriminant)/ 2*a
    return n1.is_integer() or n2.is_integer()

#let x be a hexagonal number
# 0 = 2n^2 - n - x
def isHexagonal(x):
    a = 2
    b = -1
    c = -x
    discriminant = math.sqrt((
        (b**2) - (4*a*c)
    ))
    n1 = (-b + discriminant)/ 2*a
    n2 = (-b - discriminant)/ 2*a
    return n1.is_integer() or n2.is_integer()

def generateTriangle(n):
    return (n * (n + 1)) / 2


for n in range(100000):
    y = generateTriangle(n)
    if isHexagonal(y) and isPentagonal(y):
        print(y)


#prints values after 40755 that arent the solution but a few later it is?
