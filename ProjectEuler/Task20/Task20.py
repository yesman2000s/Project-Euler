#sum of the digits of 100! 

factorial = 1

for x in range(1,101):
    factorial *= x


sum = 0
for digit in str(factorial):
    sum += int(digit)

print(sum)