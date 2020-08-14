#In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#It is possible to make £2 in the following way:

#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?

coins = [200, 100, 50, 20, 10, 5, 2, 1]
ways = 0
goal = 200

for a in range(0, goal + 1, coins[0]):
    for b in range(0, goal + 1, coins[1]):
        for c in range(0, goal + 1, coins[2]):
            for d in range(0, goal + 1, coins[3]):
                for e in range(0, goal + 1, coins[4]):
                    for f in range(0, goal + 1, coins[5]):
                        for g in range(0, goal + 1, coins[6]):
                            result = goal - a -b - c - d - e - f - g
                            if result >= 0:
                                ways += 1

print(ways)
