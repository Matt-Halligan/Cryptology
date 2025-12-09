##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 11 Assignment 11, Question 2b
# Professor Tom McGuire
#
# Elliptic Curve Digital Signature Algorithm
#
# Referenced from ECDSA.ipynb course material 
# modified to fit assignment instructions
#
##############################################


# 1) Basic parameters
p = 127                     # large prime
a = 1                       # curve coefficient
b = 26                      # curve coefficient
q = 131                     # order of base point A

# 2) Base point and keys
A = (2, 6)                  # generator of order q
m = 54                      # signer’s private key, 0 ≤ m ≤ q−1

def ec_add(P, Q):
    x1, y1 = P
    x2, y2 = Q
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
    return R

def ec_mul(n, P):
    R = None
    for m in range(1, n+1):
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
    return R

B = ec_mul(m, A)            # public key B = m·A

# 3) Signing
def Hash(x):                # placeholder SHA3-224(x)=10
    return 10

k = 75                      # ephemeral secret, 1 ≤ k ≤ q−1
x = 704101015              # message representative = 'hello'_decimal

# 3a) compute kA = (u, v)
(u, v) = ec_mul(k, A)

# 3b) r = u mod q
r = u % q
if r == 0:
    raise ValueError("r = 0, choose another k")

# 3c) s = k^{-1} · (Hash(x) + m·r) mod q
k_inv = pow(k, q-2, q)
s = (k_inv * (Hash(x) + m * r)) % q
if s == 0:
    raise ValueError("s = 0, choose another k")

print(f"Signature on message x: (r, s) = ({r}, {s})")


# 4) Verification
w = pow(s, q-2, q)          # w = s^-1 mod q
i = (w * Hash(x)) % q       # i = w · Hash(x) mod q
j = (w * r)       % q       # j = w · r       mod q

# 4a) compute U=(u, v) = i·A + j·B
U = ec_add(ec_mul(i, A), ec_mul(j, B))

# 4b) accept iff U[0] mod q == r
if U is None:
    valid = False
else:
    valid = (U[0] % q) == r

print("Verification result:", valid)

