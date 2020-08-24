#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

from itertools import permutations

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def pandigital_prime(numbers):
    for i in list(numbers)[::-1]:
        number = int(''.join(i))
        if is_prime(number):
            return number
    return 0

# 1+2+3+4+5+6+7+8+9 = 45 --> 45 is divisible by 3
# 1+2+3+4+5+6+7+8 = 36 --> 36 is divisible by 3
# 1+2+3+4+5+6+7 = 28 --> 28 is not divisible by 3
# 1+2+3+4+5+6 = 21 --> 21 is divisible by 3
# 1+2+3+4+5 = 15 --> 15 is divisible by 3
# 1+2+3+4 = 10 --> 10 is not divisible by 3
# 1+2+3 = 6 --> 6 is divisible by 3
# 1,2 --> 12 and 21 are not primes
# 1 --> is not a prime
# pandigital primes must be in 4 or 7 digits numbers

numbers_seven = permutations("1234567")
numbers_four = permutations("1234")

result = pandigital_prime(numbers_seven)
if result == 0:
    result = pandigital_prime(numbers_four)

print(result)

