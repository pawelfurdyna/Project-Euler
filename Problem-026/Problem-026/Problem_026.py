#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

d = 2
longest = 0
max_d = 0

while d < 1000:
    # Reset variables
    divident = 1
    divisor = d
    remainders = []
    recurring_cycle = ''

    # Check remainder
    # If remainder is equal to 0 it means that is no longer divisible
    # If remainder is equal to one of the previous remainders it means that it starts the cycle all over again
    while divident != 0:
        while divident // divisor == 0:
            divident = divident * 10
        if divident not in remainders:
            remainders.append(divident)
        else:
            break
        recurring_cycle += str(divident // divisor)
        divident = divident % divisor

    # Save d with longest recurring cycle
    if len(recurring_cycle) > longest:
        longest = len(recurring_cycle)
        max_d = d
    d += 1

print(max_d)