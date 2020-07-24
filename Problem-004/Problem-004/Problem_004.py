# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

num = 0

for x in range(1000):
    for y in range(1000):
        z = x * y
        if str(z) == str(z)[::-1]:
            if z > num:
                num = z

print(num)