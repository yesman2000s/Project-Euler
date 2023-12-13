prevNo = 1
currentNo = 2
fibTotal = 0

while prevNo <=4000000:

    prevNo,currentNo = currentNo, prevNo + currentNo

    if (prevNo %2) == 0:
        fibTotal += prevNo

print(fibTotal)


#4613732
