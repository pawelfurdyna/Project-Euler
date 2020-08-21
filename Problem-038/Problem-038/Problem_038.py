#Take the number 192 and multiply it by each of 1, 2, and 3:

#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def is_pandigital(n):
    nums = []
    for i in n:
        # If i is in nums or is equal to 0 there can't be solution to this problem
        if i in nums or i == "0":
            return False
        else:
            nums.append(i)
    return True

max_sum = 0

# By multipling 4-digit numbers we can get 4 or 5 digits
# 5 digit number gives 5 or 6 numbers so it can't be possibility to add products of n > 1
for i in range(99999):
    sum = ""
    for j in range(1,9):
        if len(sum) == 9:
            if is_pandigital(sum) and int(sum) > max_sum:
                max_sum = int(sum)
        sum += str(i * j)

print(max_sum)