
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

import scipy.special

side = 20

roads = scipy.special.comb(side *2, side, exact=True)
print(roads)