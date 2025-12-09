##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 1 Assignment 1, question 3b
# Professor Tom McGuire
#
# Decrypt the following ciphertext where block size m = 9:
# ANRTSEAGGYETEMNHOLOINIWGNNMONIEVTSOTBHALPWYOAGNTUOCAIESFEMAHOCESGAWSMRAE
# using the permutation key pi from part 3a.
##############################################

ciphertext = "ANRTSEAGGYETEMNHOLOINIWGNNMONIEVTSOTBHALPWYOAGNTUOCAIESFEMAHOCESGAWSMRAE"

permutation_key = [9, 5, 3, 2, 1, 7, 4, 6, 8]

# The fixed block length m
block_size = len(permutation_key)


inverse_permutation = [0] * block_size
# map indices in inverse permutation to indices in cipher position
for cipher_position, permuted_position in enumerate(permutation_key):
    inverse_permutation[permuted_position - 1] = cipher_position

# Begin collection of decrypted blocks
decrypted_blocks = []
for block_start in range(0, len(ciphertext), block_size):
    ciphertext_block = ciphertext[block_start : block_start + block_size]

    plaintext_block = "".join(
        ciphertext_block[inverse_permutation[plain_index]]
        for plain_index in range(block_size)
    )

    decrypted_blocks.append(plaintext_block)

# Join the decrypted blocks for easy printing
decrypted_plaintext = "".join(decrypted_blocks)
print(decrypted_plaintext)
