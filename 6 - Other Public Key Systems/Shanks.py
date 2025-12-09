##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 9 Assignment 9, question 1
# Professor Tom McGuire
#
# Compute the discrete logarithms in Z*_p
#
##############################################
import math

p, alpha, beta = 24691, 106, 12375
p, alpha, beta = 458009, 6, 248388

n = p - 1  # group order
m = math.ceil(math.sqrt(n))


L1 = []
for j in range(m):
    value = pow(alpha, m * j, p)
    L1.append((j, value))
L1.sort(key=lambda pair: pair[1])


alpha_inv = pow(alpha, p - 2, p)  # modular inverse of alpha mod p
L2=[]
for i in range(m):
    value = (beta * pow(alpha_inv, i, p)) % p
    L2.append((i, value))
    
L2.sort(key=lambda pair: pair[1])

i1 = 0
i2 = 0
while i1 < m and i2 < m:
    j, val1 = L1[i1]
    i, val2 = L2[i2]
    if val1 == val2:
        y = (j * m + i) % n
        break
    elif val1 < val2:
        i1 += 1
    else:
        i2 += 1
if y:
    print(f"log_{alpha}({beta}) mod {p} = {y}")
