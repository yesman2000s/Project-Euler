

def seq(n):
    return n * (n+1) * 0.5

triangleNumbers = [seq(x) for x in range(1,10000)]  

def isWordTriangle(word:str):
    word = word
    sum = 0
    for x in word:
        sum += ord(x) - 64
    return sum in triangleNumbers


found = 0

with open("Task42\Words.txt","r") as words:
    allwords = words.readlines()[0].split(",")
    for x in allwords:
        word = x.removeprefix("\"").removesuffix("\"")
        if isWordTriangle(word):
            found += 1

print(found)
