##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 7 Assignment 7, question 2
# Professor Tom McGuire
#
# Compute the Exponentiation using the Square and Multiply Algorithm
# 
##############################################

#base = 2405210030
#exponent = 65537
#modulus = 2993725127

#base = 1977
#base = 3164
#base = 2776
#base = 11719
#base = 16450
#base = 3913
exponent = 65537
modulus = 190219


z = 1
# Process bits of c from most-significant down to least
for bit in bin(exponent)[2:]:
    # square step
    z = (z * z) % modulus
    # multiply step if the current bit is 1
    if bit == '1':
        z = (z * base) % modulus

print(f"Exponentiation: {z}")
