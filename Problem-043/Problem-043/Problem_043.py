#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations

numbers = permutations("0123456789")
sum = 0
for i in list(numbers):
        # Create permutations
        number = int(''.join(i))
        if len(str(number)) == 10:
            # Add sub-strings to list
            substring = []
            substring.append(str(number)[1] + str(number)[2] + str(number)[3])
            substring.append(str(number)[2] + str(number)[3] + str(number)[4])
            substring.append(str(number)[3] + str(number)[4] + str(number)[5])
            substring.append(str(number)[4] + str(number)[5] + str(number)[6])
            substring.append(str(number)[5] + str(number)[6] + str(number)[7])
            substring.append(str(number)[6] + str(number)[7] + str(number)[8])
            substring.append(str(number)[7] + str(number)[8] + str(number)[9])
            # Remove 0 from start of sub-string
            for j in range(len(substring)):
                if substring[j][0] == '0':
                    substring[j] = substring[j][1]+substring[j][2]
            # Check property of sub-strings and to the sum if true
            if int(substring[0]) % 2 == 0 and int(substring[1]) % 3 == 0 and int(substring[2]) % 5 == 0 and int(substring[3]) % 7 == 0 and int(substring[4]) % 11 == 0 and int(substring[5]) % 13 == 0 and int(substring[6]) % 17 == 0:
                sum += number

print(sum)