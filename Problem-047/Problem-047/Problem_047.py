#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

def len_of_div(n):
    prime = 2
    div = set()
    while prime < n**0.5 or n == 1:
        if n % prime == 0:
            n = n/prime
            div.add(prime)
            prime -= 1
        prime += 1
    return len(div)+1

number = 2*3*5*7

while True:
    if len_of_div(number) == 4:
        number += 1
        if len_of_div(number) == 4:
            number += 1
            if len_of_div(number) == 4:
                number += 1
                if len_of_div(number) == 4:
                    print(number-3)
                    break
    number += 1