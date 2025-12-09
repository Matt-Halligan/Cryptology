##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 8 Assignment 8, question 5
# Professor Tom McGuire
#
# Compute the system of congruences using the Chinese Remainder Theorem Algorithm
# 
##############################################

moduli    = [25777, 22879, 66277]
remainders = [19052, 4546, 44619]
remainders = [1708, 11733, 19731]
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
