#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from math import factorial

def num_list(digits):
    num = []
    for i in range(digits + 1):
        num.append(i)
    return num

def finding_permutation(digits, n, num):
    perm = n - 1
    x = digits
    result = ""
    while x >= 0:
        remainder = int(perm % factorial(x))
        perm = int(perm // factorial(x))
        result += str(num[perm])
        num.remove(num[perm])
        perm = remainder
        x -= 1
    return result

def main(digits, n):
    num = num_list(digits)
    result = finding_permutation(digits, n, num)
    print(result)

digits = 9
n = 1000000
main(digits, n)