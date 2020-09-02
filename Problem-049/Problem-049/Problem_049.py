#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?

def is_prime(n):
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(n):
    primes = [2,3]
    for i in range(4, n):
        if is_prime(i):
            primes.append(i)
    return primes

# List of numbers in prime
def str_char(s):
    chars = []
    for c in str(s):
        chars.append(c)
    chars.sort()
    return chars

#Create list of primes up to 10000
primes = prime_numbers(10000)
prime_check = []

#List of primes between 1487 and 9999
for prime in primes:
    if prime > 1487:
        prime_check.append(prime)

for i in range(1, len(prime_check)):
    for j in range(i + 1, len(prime_check)):
        # Check difference between i and j and find in list of primes
        if prime_check[j] + (prime_check[j] - prime_check[i]) in prime_check:
            # Check numbers in primes - true if they are permutations of one another
            if str_char(prime_check[i]) == str_char(prime_check[j]) and str_char(prime_check[i]) == str_char(prime_check[j] + (prime_check[j] - prime_check[i])):
                # Print 12 digit number
                print(str(prime_check[i]) + str(prime_check[j]) + str(prime_check[j] + (prime_check[j] - prime_check[i])))

