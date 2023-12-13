
LargestNumber = 1
UptoNum = 21

def Divisible(number):
    for num in range(1,UptoNum):
        if (number%num) == 0:
            continue
        else:
            return False
    return True

#largest possible number
for num in range(1,UptoNum):
    LargestNumber *= num



smallest = 1
for num in range(1,LargestNumber,1):
    if str(num)[-1] != "0":
        continue
    
    if Divisible(num):
        print("yes",num)
        smallest = num
        break

print(smallest)

#answer yes 232792560
#232792560
