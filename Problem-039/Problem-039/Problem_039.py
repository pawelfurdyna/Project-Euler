#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p ≤ 1000, is the number of solutions maximised?

def right_triangle(a,b,c,n):
    if a**2 + b**2 == c**2:
        return True
    return False

p = 4
max_p = 0
max_solution = 0
while p < 1000:
    solution = 0
    # a will be max in 1/4 value of p
    for a in range(1,int(p/4)+1):
        # c can be max (1/2 * p) - 1 --> 1/2*p
        # because b > a, a + b > c and a**2 + b**2 = c**2
        # b must be in range from a to ((1/2 * p)**2 - a**2) ** 1/2 
        for b in range(a,int((1/4 * p**2 - a**2)**(1/2))):
            # Check for a + b + c = p
            c = p - a - b
            if right_triangle(a,b,c,p):
                solution += 1
    if solution > max_solution:
        max_solution = solution
        max_p = p
    p += 1

print(max_p)