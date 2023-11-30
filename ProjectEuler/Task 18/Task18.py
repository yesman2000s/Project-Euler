triangleString = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
splitTriangle = triangleString.split("\n")
triangleArray = []

for row in splitTriangle:
    if row == "":
        continue
    
    arrayOfDigits = []
    stringOfDigits = row
    digits = stringOfDigits.split(" ")

    for number in digits:
        arrayOfDigits.append(int(number))

    triangleArray.append(arrayOfDigits)

#flip array
triangleArray = triangleArray[::-1]

countLength = len(triangleArray) - 1

for row in range(0, countLength, 1):
    #in each row
    rowLength = len(triangleArray[row]) - 1
    for numberIndex in range(0,rowLength):
        rowAboveIndex = row + 1
        numberAboveIndex = numberIndex

        currentNumber = triangleArray[row][numberIndex]
        nextNumber = triangleArray[row][numberIndex + 1]

        triangleArray[rowAboveIndex][numberAboveIndex] += max(currentNumber , nextNumber)
print(triangleArray)

#reverse order
#max between index and next index
#sum it with the index directly above
"""
         [75]
       [95,64]
    [17, 47, 82]
[20, 4, 82, 47, 65]
"""