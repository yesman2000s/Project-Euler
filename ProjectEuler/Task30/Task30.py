
founds = []
for x in range(2,500000):
    tostr = str(x)
    sumofdigits = 0
    for digit in tostr:
        sumofdigits += int(digit)**5
    if x == sumofdigits:
        founds.append(x)
print(sum(founds))
