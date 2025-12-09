##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 10 Assignment 10, question 3a
# Professor Tom McGuire
#
# Simple Elliptic Curve Private Key searcher
#
##############################################

#Parameters
p = 4339
a = 193
b = 647

# Points
P = (719, 3538)
Q = (3509, 334)

# Brute-force find m up to max_m such that m*P = Q
R = None
found = False
max_m = 4000
for m in range(1, max_m):
    # R = R + P
    if R is None:
        R = P
    else:
        x1, y1 = R
        x2, y2 = P
        # Case 2
        if x1 == x2 and (y1 + y2) % p == 0:
            R = None
        else:
            # Case 3
            if x1 == x2 and y1 == y2:
                num = (3*x1*x1 + a) % p
                den = pow(2*y1 % p, p-2, p)
            #Case 1
            else:
                num = (y2 - y1) % p
                den = pow((x2 - x1) % p, p-2, p)
            lam = (num * den) % p
            x3 = (lam*lam - x1 - x2) % p
            y3 = (lam*(x1 - x3) - y1) % p
            R = (x3, y3)
    # check match
    if R == Q:
        print(f"Found private key: m = {m}")
        found = True
        break
if not found:
    print(f"No m up to {max_m} produces Q.")
