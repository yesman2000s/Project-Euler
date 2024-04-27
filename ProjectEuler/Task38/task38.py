def isPandigital(digit:str):
    return sorted(digit) == list('123456789')

#keep multiplying number until when concatenated the products are
# == 9 in length.
#cast it and compare.
 

largest = 0

for number in range(1,10000):
    concatenatedProduct = ""
    multipland = 1
    
    while True:
        concatenatedProduct += str(number*multipland)
        multipland += 1
        if len(concatenatedProduct) == 9:
            if isPandigital(concatenatedProduct):
                if int(concatenatedProduct) > int(largest):
                    largest = concatenatedProduct
        elif len(concatenatedProduct) > 9:
            break

print(largest)
