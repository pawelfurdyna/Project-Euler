#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

def is_prime(n, primes):
    for i in primes:
        if n % i == 0:
            return False
    return True

# Check primes by dividing numbers by primes before this number
def prime_list():
    n = 3
    primes = [2]
    while n < 1000000:
        if is_prime(n, primes):
            primes.append(n)
        n += 2
    return primes

# Removing primes which are divisible by 2 or 5
def check_primes(primes):
    primes_remove = []
    for prime in primes:
        for num in str(prime):
            if int(num) % 2 == 0 or int(num) == 5:
                primes_remove.append(prime)
    for i in range(len(primes_remove)):
        if primes_remove[i] in primes:
            primes.remove(primes[primes.index(primes_remove[i])])
    primes.append(2)
    primes.append(5)
    primes.sort()
    return primes


primes = check_primes(prime_list())

counter = 0
for i in primes:
		length = len(str(i))
		number = i
		counter += 1
		# Circular permutations
		for j in range(length):
			number = (number%10)*10**(length-1)+number//10
			# If any permutation is not prime subtract one from counter
			if number not in primes:
				counter -= 1
				break

print(counter)

