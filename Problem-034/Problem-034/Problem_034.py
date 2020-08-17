#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: As 1! = 1 and 2! = 2 are not sums they are not included.

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n - 1)

factorials = []
for i in range(1, 10):
    factorials.append(factorial(i))

total = 0
for i in range(10, 2000000):
    sum = 0
    for fact in str(i):
        if fact == '0':
            sum += 1
        else:
            sum += factorials[int(fact) - 1]
    if sum == i:
        total += i


print(total)