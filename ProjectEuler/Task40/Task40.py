digit = ""
for x in range(1,200_000):
    digit += str(x)

positions = [1,10,100,1000,10_000,100_000,1_000_000]

answer = 1
for x in positions:
    answer *= int(digit[x-1])

print(answer)