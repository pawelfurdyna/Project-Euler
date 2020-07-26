# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True

sum = 2

for i in range(3, 2000000):
    if isPrime(i):
        sum += i

print(sum)