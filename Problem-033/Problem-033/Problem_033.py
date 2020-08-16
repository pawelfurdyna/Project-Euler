#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def simplify(a, b):
    num = str(a)[1]
    # Check second number from numerator
    # Must be equal to first from denominator
    # Can't be equal to first ( 11 / 11 is equal to 1/1) 
    if num == str(b)[0] and num != str(b)[1]:
        # Remove duplicate
        a = int(str(a).replace(num, '', 1))
        b = int(str(b).replace(num, '', 1))
        # Denominator can't be 0
        if b == 0:
            return 0
        return a/b  

product = 1
for i in range(11,100):
    for j in range(11,100):
        if i/j == simplify(i, j):
            product /= simplify(i, j)

print(int(product))


