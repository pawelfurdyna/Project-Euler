#The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)

def palindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

def dec_palindroms():
    decimal_palindroms = []
    for i in range(1, 1000000):
        if palindrom(i):
            decimal_palindroms.append(i)
    return decimal_palindroms

def bin_convert(n):
    i = 0
    num = n
    bin = ''
    # Find first power that is greater than number
    while 2**i <= num:
        i += 1
    # Power that is in range of number
    i -= 1
    while i >= 0:
        # If power of 2 is less or equal to number add 1 to string
        if num // (2**i) == 1:
            bin += '1'
            num = num % (2**i)
        # If is smaller add 0 to string
        else:
            bin += '0'
        i -= 1
    return bin

decimal_palindroms = dec_palindroms()
sum = 0
for i in decimal_palindroms:
    bin = bin_convert(i)
    if palindrom(bin):
        sum += i

print(sum)