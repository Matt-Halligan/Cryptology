##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 7 Assignment 7, question 3
# Professor Tom McGuire
#
# Compute the system of congruences using the Chinese Remainder Theorem Algorithm
# 
##############################################

moduli    = [163659, 146921, 193331]
remainders = [29683, 144995, 136776]

# Compute the product of all moduli
M = 1
for m in moduli:
    M *= m
print(f"moduli: {M}")
# Build the solution
x = 0
for a, m in zip(remainders, moduli):
    Mi = M // m                    # Partial product
    yi = pow(Mi, -1, m)            # Modular inverse of Mi mod m
    x += a * Mi * yi               # Accumulate

# Reduce modulo M
x %= M

print("Solution x =", x)
