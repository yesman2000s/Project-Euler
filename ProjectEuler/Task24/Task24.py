numbers = [0,1,2,3,4,5,6,7,8,9]


def isEven(Number):
    return (Number%2) == 0


def generatePermutations(numbersList , length):
    if length == 1:
        print(numbersList)
    else:
        # Generate permutations with k-th unaltered
        # Initially k = length(A)
        generatePermutations(numbersList , length - 1)

        for x in range(1,length):
            if isEven(length):
                numbersList[x] , numbersList[length-1] = numbersList[length-1] , numbersList[x] 
            else:
                numbersList[0] , numbersList[length-1] = numbersList[length-1] , numbersList[0] 
        generatePermutations(numbersList,length-1)
        
        print(numbersList)
generatePermutations([1,2,3,4] , 2)