numbers = [0,1,2,3,4,5,6,7,8,9]


def isEven(Number):
    return (Number%2) == 0

foundPermutations = []

def generatePermutations(numbersList, length):
        if length == 1:
            # A permutation was found!!
            print(numbersList)
            foundPermutations.append(numbersList.copy())
        else:
            # Generate permutations with k-th unaltered
            # Initially k = length(A)
            generatePermutations(numbersList, length - 1)

            for x in range(length - 1):
                if isEven(length):
                    # Swap elements at x and length-1
                    numbersList[x], numbersList[length-1] = numbersList[length-1], numbersList[x]
                else:
                    # Swap elements at 0 and length-1
                    numbersList[0], numbersList[length-1] = numbersList[length-1], numbersList[0]
                generatePermutations(numbersList, length - 1)

generatePermutations([0,1,2],3)
print(foundPermutations)