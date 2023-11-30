def getNameValue(name):
    total = 0
    for x in name:
        total += ord(x) - 64
    return total


names = open(r"C:\Users\Owner\OneDrive\Documents\PythonProjects\ProjectEuler\Task22\NAMES.txt" , 'r').read()

namesArray = names.split(",")

for name in range(len(namesArray)):
    namesArray[name] = namesArray[name].replace("\"","") 

namesArray = sorted(namesArray)

total = 0
for x in range(len(namesArray)):
    nameSum = getNameValue(namesArray[x]) * (x+1)
    total += nameSum    
    if namesArray[x] == "COLIN":
        print(getNameValue(namesArray[x]) , x+1)

print(total)
