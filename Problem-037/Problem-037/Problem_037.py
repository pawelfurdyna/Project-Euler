#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def is_prime(n, primes):
    for i in primes:
        if n % i == 0:
            return False
    return True

# Removing numbers
# // for numbers from right
# % for numbers from left
def right_remove(prime, primes):
    for i in range(1, len(str(prime))):
        if prime // (10**i) not in primes:
            return False
    return True

def left_remove(prime, primes):
    for i in range(1, len(str(prime))):
        if prime % (10**i) not in primes:
            return False
    return True

def counting(n, primes, result):
    if left_remove(n, primes) and right_remove(n, primes):
        result[1] += n
        result[0] += 1
    return result


def prime_list():
    # Start from 11 and add first four primes to the list
    n = 11
    primes = [2, 3, 5, 7]
    # List for storage numbers for counter and sum
    result = [0, 0]
    start = True
    while start:
        if is_prime(n, primes):
            primes.append(n)
            result = counting(n, primes, result)
            if result[0] == 11:
                start = False
                print(result[1])
        n += 2
    return primes

primes = prime_list()