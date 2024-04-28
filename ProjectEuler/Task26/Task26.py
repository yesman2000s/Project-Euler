def cycleLength(d):
    n = 1 
    remainders = []
    while len(remainders) == len(set(remainders)):
        remainder = n % d
        remainders.append(remainder)
        n = remainder * 10
    return len(set(remainders))

longest = 0
d = 0

for x in range(1,1000):
    if cycleLength(x) > longest:
        longest = cycleLength(x)
        d = x

print(d)