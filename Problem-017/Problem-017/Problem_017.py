#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

numbers = {
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine"),
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen"),
    20: len("twenty"),
    30: len("thirty"),
    40: len("forty"),
    50: len("fifty"),
    60: len("sixty"),
    70: len("seventy"),
    80: len("eighty"),
    90: len("ninety"),
    100: len("onehundred"),
    200: len("twohundred"),
    300: len("threehundred"),
    400: len("fourhundred"),
    500: len("fivehundred"),
    600: len("sixhundred"),
    700: len("sevenhundred"),
    800: len("eighthundred"),
    900: len("ninehundred"),
    1000: len("onethousand")
    }

sum = 0

for i in range(1, 1001):
    if len(str(i)) == 4:
        sum += numbers[1000]
    elif len(str(i)) == 3:
        hundreds = int(str(i)[0] + "00")
        if i % 100 == 0:
            sum += numbers[hundreds]
        else:
            sum += numbers[hundreds] + 3
            tens = int(str(i)[1] + "0")
            if int(str(i)[1:3]) <= 20:
                sum += numbers[int(str(i)[1:3])]
            else:
                sum += numbers[tens]
                ones = int(str(i)[2])
                if ones != 0:
                    sum += numbers[ones]
    elif len(str(i)) == 2:
        tens = int(str(i)[0] + "0")
        if i <= 20:
            sum += numbers[i]
        else:
            sum += numbers[tens]
            ones = int(str(i)[1])
            if ones != 0:
                sum += numbers[ones]
    else:
        sum += numbers[i]

print(sum)