import math

def isRightTriangle(a,b):
    c = math.sqrt(a**2 + b**2)
    return c == int(c) , int(c)

answers = [0] * 1001

for a in range(1,1001):
    for b in range(1,1001):
        isTriple , c = isRightTriangle(a,b)
        perimiter = a+b+c
        if isTriple and perimiter <= 1000:
            answers[perimiter] += 1

max = 0 
maxvalue = 0
for x in range(len(answers)):
    if answers[x] > max:
        max = answers[x]
        maxvalue = x
print(maxvalue)
