#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

numbers = ''
for i in range(1000001):
    numbers += str(i)

result = int(numbers[1]) * int(numbers[10]) * int(numbers[100]) * int(numbers[1000]) * int(numbers[10000]) * int(numbers[100000]) * int(numbers[1000000])
print(result)