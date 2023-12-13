lengths = {}

def OddOrEven(number):
    return (number%2)==0

def Collatz(Number):
    a = Number
    length = 1
    while Number != 1:
        #if the numbers collatz chain length has already been solved
        #add it to the length.

        if Number in lengths:
            lengths[a] = length + lengths[Number]
            return
        
        if OddOrEven(Number):
            Number = Number / 2
        else:
            Number = Number*3 + 1
        length += 1
    lengths[a] = length

for x in range(2,10**6):
    Collatz(x)

print(max(zip(lengths.values(), lengths.keys()))[1])



