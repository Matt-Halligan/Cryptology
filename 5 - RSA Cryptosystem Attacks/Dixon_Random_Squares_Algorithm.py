##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 8 Assignment 8, question 4 
# Professor Tom McGuire
#
# Dixon's Algorithm on 600 <= z <= 660
#
##############################################
from collections import Counter

B = [-1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
n=347881
for z in range(600, 661):
    factors = []
    z_congru=((n-(z**2))%n)-(n)
    original = z_congru
    if z_congru < 0:
        factors.append(-1)
        z_congru = -z_congru
    for p in B:
        if p == -1:
            continue
        # keep dividing while p | n
        while z_congru % p == 0:
            factors.append(p)
            z_congru //= p
    cnt = Counter(factors)
    vector = tuple(cnt[p] for p in B)
    product = 1
    for f in factors:
        product *= f
    if product == original:
        print(product, "==" , z_congru)
        print(f"z={z}: {original}={'*'.join(str(f) for f in factors)}={vector}")
