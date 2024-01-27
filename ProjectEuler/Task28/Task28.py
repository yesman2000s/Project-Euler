dimension = 1001


total = 1
for x in range(dimension,1,-2):
    for y in range(0,4):
        total += x**2 - ((x*y) - (y*1))

print(total)
