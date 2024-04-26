def isPalindrome(string):
    return string == string[::-1]

sumof = 0

for x in range(0,1_000_000):
    binary = bin(x).replace("0b","")
    if binary[0] == '1':
        if isPalindrome(str(x)) and isPalindrome(binary):
            sumof += x

print(sumof)