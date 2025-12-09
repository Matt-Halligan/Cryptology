##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 11 Assignment 11, question 2a
# Professor Tom McGuire
#
# Simple Elliptic Curve DSA Public Key Calculator
# returns B=mA
#
##############################################

p = 127
a = 1
b = 26
max_m=54
A = (2, 6)
R = None
P = A

for m in range(1, max_m+1):
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
B = R

print(f"The public key B = mA = {B}")
