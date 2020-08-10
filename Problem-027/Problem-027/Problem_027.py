#Euler discovered the remarkable quadratic formula:
#n**2 + n + 41

#It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

#The incredible formula n**2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.

#Considering quadratics of the form:

#n**2 + an + b, where |a| < 1000 and |b| <= 1000

#where |n| is the modulus/absolute value of n
#e.g. |11| = 11 and |-4| = 4
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

# Checking if it is a prime number
def is_prime(n):
    for i in range(2, abs(n)):
        if n % i == 0:
            return False
    return True

# Creating list of prime numbers (positive and negative)
def prime_numbers(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
            primes.append(-i)
    primes.sort()
    return primes

def quadratic_formula(primes):
    # Variables for max value
    max_n = 0
    max_a = 0
    max_b = 0

    # Iteration through a lost of primes
    for a in primes:
        for b in primes:
            n = 0
            # If the result is prime add 1 to n
            while is_prime(n**2 + a * n + b):
                n += 1
            #  If not check that n is greater than the previous maximum value
            if n > max_n:
                max_n = n
                max_a = a
                max_b = b
                print(a)
                print(b)
                print(n)
                print("")
    return max_a * max_b

primes = prime_numbers(1000)
product = quadratic_formula(primes)
print(product)