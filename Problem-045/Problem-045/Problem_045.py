#Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

#Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
#Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
#Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
#It can be verified that T285 = P165 = H143 = 40755.

#Find the next triangle number that is also pentagonal and hexagonal.

def is_triangle(number):
    check = 0
    n = int((number/2)**(1/2))
    while number > check:
        check = (n * (n + 1) / 2)
        if  check == number:
            return True
        n += 1
    return False

def is_pentagonal(number):
    check = 0
    n = int((number/2)**(1/2))
    while number > check:
        check = (n * (3*n - 1) / 2)
        if  check == number:
            return True
        n += 1
    return False

def hexagonal(number):
    return number * (2*number - 1)

n = 143
start = True

while start:
    n += 1
    number = hexagonal(n)
    if is_triangle(number) and is_pentagonal(number):
        start = False

print(number)