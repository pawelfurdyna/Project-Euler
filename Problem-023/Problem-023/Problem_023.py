#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


# Global var
abundants = []
sum_notfound = 0

# Creating list of abundant numbers
def sum_divs(n):
    sum = 0
    for i in range(1, int((n/2) + 1)):
        if n % i == 0:
            sum += i
    return sum

for n in range(11, 28123):
    if sum_divs(n) > n:
        abundants.append(n)

# Finding possible sum of abundant numbers
def found_sum(n):
    for a in abundants:
        remaining = n - a
        if search(abundants, remaining):
            return True
    return False

# Binary search for remaining part
def search(list, num):
    found = False
    up = len(list)-1
    low = 0

    while not found and low <= up:
        mid = int((low+up)/2)
        if list[mid] == num:
            found = True
        elif list[mid] < num:
            low = mid + 1
        else:
            up = mid - 1
    return found

# Sum of all numbers that cannot be a combination of two abundant numbers
for j in range(1, 28124):
    if not found_sum(j):
        sum_notfound += j

print(sum_notfound)