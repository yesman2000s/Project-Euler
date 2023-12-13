#get sum of the squares

SumOfSquares = 0
SquareOfSum = 0
for num in range(1,101):
    SumOfSquares += (num*num)
    SquareOfSum += num

SquareOfSum *= SquareOfSum

print(SquareOfSum - SumOfSquares)
#25164150
