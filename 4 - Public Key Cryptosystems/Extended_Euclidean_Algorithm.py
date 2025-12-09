##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 7 Assignment 7, question 1
# Professor Tom McGuire
#
# Compute the Multiplicative Inverses
# 
##############################################

# uncomment a,b pair for specific problem statement

#a=87276
#b=186270

#a=527667751
#b=2297634964

#a=41586933446220082872168792411016360390278592380680477028872096588587928594989
#b=5010609569443118167691454968557827442659503676125410711002434917434601365503

a=65537
b=189144

a0, b0 = a, b
t0, t = 0, 1
s0, s = 1, 0

# First quotient and remainder
q = a0 // b0
r = a0 - q * b0

# Main loop
while r > 0:
    # Update t's
    temp = t0 - q * t
    t0, t = t, temp

    # Update s's
    temp = s0 - q * s
    s0, s = s, temp

    # Shift a0, b0 and recompute q, r
    a0, b0 = b0, r
    q = a0 // b0
    r = a0 - q * b0

# When loop ends, b0 is the gcd
r = b0

print(f"gcd({a},{b}) = {r}")
print(f"Coefficients: {s}*{a} + {t}*{b} = {r}")
