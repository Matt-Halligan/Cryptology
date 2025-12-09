##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 4 Assignment 4, question 2a
# Professor Tom McGuire
#
# Compute the table values of N_D
# 
##############################################

# S-box definition
s_box = {
    0x0: 0xF,
    0x1: 0x0,
    0x2: 0xB,
    0x3: 0xD,
    0x4: 0x1,
    0x5: 0xC,
    0x6: 0x6,
    0x7: 0xE,
    0x8: 0x2,
    0x9: 0x9,
    0xA: 0x8,
    0xB: 0x4,
    0xC: 0x5,
    0xD: 0xA,
    0xE: 0x3,
    0xF: 0x7
}

# Build the N Differential Distribution Table
Nd_table = [[0]*16 for _ in range(16)]
for u_prime in range(16):
    for z in range(16):
        z_star = z ^ u_prime
        v      = s_box[z]
        v_star = s_box[z_star]
        v_prime = v ^ v_star
        Nd_table[u_prime][v_prime] += 1



header = "u'/v'"
print(header, [v_prime for v_prime in range(16)])
print()
for u_prime in range(16):
    print(u_prime, "\t", Nd_table[u_prime])
