# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

i = 2
n = 3

while i < 10002:
    for num in range(2,n):
        if (n % num) == 0:
            n += 1
            break
    else:        
        i += 1
        n += 1
        
print(n-1)