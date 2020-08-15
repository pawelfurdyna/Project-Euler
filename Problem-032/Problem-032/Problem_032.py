#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

sum = 0
result = []

def is_pandigital(n):
    nums = []
    for i in n:
        # If i is in nums or is equal to 0 there can't be solution to this problem
        if i in nums or i == "0":
            return False
        else:
            nums.append(i)
    return True

for i in range(1,1000):
    for j in range(1, 10000):
        s = str(i) + str(j) + str(i * j)
        if is_pandigital(s) and len(s) == 9:
            if (i*j) not in result:
                result.append(i*j)
        elif len(s) > 9:
            break

for i in result:
    sum += i

print(sum)