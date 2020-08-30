#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#9 = 7 + 2×1**2
#15 = 7 + 2×2**2
#21 = 3 + 2×3**2
#25 = 7 + 2×3**2
#27 = 19 + 2×2**2
#33 = 31 + 2×1**2

#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def is_prime(n):
    for i in range(2,int(n/2)):
        if n % i == 0:
            return False
    return True

start = True
n = 9

while start:
    # Check for odd composite numbers
    if not is_prime(n):
        # Find max twice a square
        i = 1
        twice_square = 0
        while twice_square < n:
            twice_square = 2*i**2
            i += 1
        # Check difference between every twice a square and n for primes
        # If there isn't any combination of prime and twice a square leave while loop
        for a in range(1, i-1):
            if is_prime(n - 2*a**2):
                start = True
                break
            else:
                start = False
    n += 2

print(n-2)