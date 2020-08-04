#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

a = 4
sum = 0

while a < 10000:
    sum_da = 0
    sum_db = 0

    for i in range(1, a):
        if a % i == 0:
            sum_da += i

    for j in range (1, sum_da):
        if sum_da % j == 0:
            sum_db += j

    if sum_db == a and a != sum_da:
        sum += sum_da

    a += 1

print(sum)