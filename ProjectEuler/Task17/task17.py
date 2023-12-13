
ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def NumberToWords(Number):
    if Number >= 1 and Number <20:
        Ones = ONES[Number]
        return Ones
    elif 20 <= Number < 100:
        Tens = TENS[Number//10]
        Units = ONES[Number%10]

        if not Units:
            return Tens
        else:
            return Tens + Units
    elif Number >= 100 and Number <1000:
        Hundreds = ONES[Number//100]
        Rest = NumberToWords(Number%100)
        if Rest:
            return Hundreds + "hundred" + "and" + Rest
        else:
            return Hundreds + "hundred"
    elif Number == 1000:
        return "onethousand"
length = 0
for x in range(1,1001):
    word = NumberToWords(x)
    print(word)
    print(len(word))
    length += len(word)
print(length)
