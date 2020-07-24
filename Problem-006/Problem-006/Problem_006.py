# The sum of the squares of the first ten natural numbers is 385 
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumsq = 0
sqsum = 0
sum = 0

for i in range(1, 101):
    sumsq += i ** 2
    sum += i

sqsum = sum ** 2

print(sqsum - sumsq)