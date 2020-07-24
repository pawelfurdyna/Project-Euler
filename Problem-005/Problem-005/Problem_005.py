# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

nums = 20
i = 1
run = True

while run:
    for num in range(1, nums + 1):
        if num == nums and i % num == 0:
            print(i)
            run = False
            break
        elif i % num == 0:
            continue
        else:
            i += 1
            break
