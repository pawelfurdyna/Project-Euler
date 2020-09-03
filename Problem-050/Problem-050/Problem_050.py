#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

n = 1000000
primes = prime_numbers(n)
max_sum = 0
max_count = 0

for i in range(0, len(primes)):
    count = 0
    sum = 0
    for j in range(i, len(primes)):
        sum += primes[j]
        if sum > n:
            break
        count += 1
        if is_prime(sum):
            if count > max_count:
                max_count = count
                max_sum = sum
print(max_sum)