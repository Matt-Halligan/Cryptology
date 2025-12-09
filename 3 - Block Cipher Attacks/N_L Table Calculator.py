##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 4 Assignment 4, question 1a
# Professor Tom McGuire
#
# Compute the table values of N_L
# 
##############################################

s_box = {
    0x0: 0x7,
    0x1: 0x3,
    0x2: 0xA,
    0x3: 0x5,
    0x4: 0x4,
    0x5: 0x8,
    0x6: 0x9,
    0x7: 0x2,
    0x8: 0xE,
    0x9: 0x6,
    0xA: 0xC,
    0xB: 0x1,
    0xC: 0xD,
    0xD: 0xB,
    0xE: 0x0,
    0xF: 0xF
}


def inner_prod(m, n):
    # count 1-bits in (m & n), then mod 2
    return bin(m & n).count("1") & 1

# Build the linear approximation table
# N_L[a][b] = sum_x (-1)^(inner_prod(a,x) XOR inner_prod(b, S(x)))
N_L = [[0]*16 for _ in range(16)]
for a in range(16):
    for b in range(16):
        count = 0
        for x in range(16):
            if inner_prod(a, x) == inner_prod(b, s_box[x]):
                count += 1
        N_L[a][b] = count


print([b for b in range(16)])
for a in range(16):
    string = f"{a}\t"
    for b in range(16):
        string += f"{N_L[a][b]}\t"
    #print(a, [f"{N_L[a][b]}\t" for b in range(16)])
    print(string)
