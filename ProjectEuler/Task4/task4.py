LargestPalindrome = 0

for x in range(100,1000,1):
    for y in range(100,1000,1):
        product = x*y
        if str(product)[::-1] == str(product):
            if product > LargestPalindrome:
                LargestPalindrome = product

print(f"The largest palindrome is {LargestPalindrome}")

#906609 -- answer
