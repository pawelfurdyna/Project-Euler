#Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

#1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

#It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

def is_pentagonal(pn):
    pn_check = 0
    n = int((pn/2)**(1/2))
    while pn > pn_check:
        pn_check = (n * (3*n - 1) / 2)
        if  pn_check == pn:
            return True
        n += 1
    return False

pentagonal_numbers = [1]
d = 0
n = 1
while d == 0:
    n += 1
    pn = int(n * (3 * n - 1) / 2)
    for i in pentagonal_numbers:
        if is_pentagonal(pn + i) and is_pentagonal(pn - i):
            d = abs(pn - i)
    pentagonal_numbers.append(pn)

print(d)