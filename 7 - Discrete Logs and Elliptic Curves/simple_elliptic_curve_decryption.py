##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 10 Assignment 10, question 3b, 3c
# Professor Tom McGuire
#
# Simple Elliptic Curve Decryption
#
##############################################

ciphertext =[((3103, 1), 1860), ((745, 1), 1308), ((2214, 0), 981), ((3210, 0), 3601), ((1222,
0), 3579), ((3643, 0), 2402), ((1449, 0), 1871), ((3450, 1), 584), ((556, 1),
3019), ((3945, 0), 148), ((468, 0), 4242), ((277, 0), 2557), ((1460, 0), 3434),
((711, 0), 1522), ((3034, 1), 3293), ((1565, 0), 848)]
#Parameters
p = 4339
a = 193
b = 647
max_m=3835
Q = (3509, 334)

qr_test_exponent = (p - 1) // 2
sqrt_exponent   = (p + 1) // 4

def modular_exponentiation(base, exponent, modulus):
    z = 1
    # Process bits of c from most-significant down to least
    for bit in bin(exponent)[2:]:
        # square step
        z = (z * z) % modulus
        # multiply step if the current bit is 1
        if bit == '1':
            z = (z * base) % modulus

    #print(f"Exponentiation: {z}")
    return z

def point_decompress(x, parity):
    z = (x*x*x+a*x+b)%p
    qr_test = modular_exponentiation(z, qr_test_exponent, p)
    if qr_test == 1:
        y = modular_exponentiation(z, sqrt_exponent, p)
        y_neg = -y % p
        if parity == 0:
            return (x, y)
        elif parity == 1:
            return (x, y_neg)
    else:
        raise ValueError("not a square")
    

def int_to_text(message):
    letter = chr((message % 26) + ord('a'))
    return letter

encoded = []
for cipher in ciphertext:
    x = cipher[0][0]
    parity = cipher[0][1]
    cipher_y = cipher[1]
    P = point_decompress(x, parity)
    R = None
    
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
    
    x0, y0 = R
    dec = cipher_y*pow(x0, p-2, p)%p
    encoded.append(dec-1)
print(encoded)
plaintext = ''.join(int_to_text(m) for m in encoded)

print("Decrypted plaintext:\n", plaintext)    

