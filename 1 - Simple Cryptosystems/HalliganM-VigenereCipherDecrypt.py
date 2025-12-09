##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 1 Assignment 1, question 6
# Professor Tom McGuire
#
# Decrypt the following Vigenere encrypted ciphertext
# BNWEOMZOBNTALBAECJHKXSFGYZXMBNBVZSBXMETRRTNOLTUWGXKOTJTUFIAYFCLT
# OWMPXPEGVMLSBXICMTVFZBAEZAGMWSTWKLBJXKMZTDRTNOZIAYBAMWVUXILHNJWI
# LWEAMQGGGZXKHDRAGBAESAKAMPYSVMMHRJXNHRRAYGHUJJBBXTUWVWWENKVTXVRJ
# EGTSCGLABBYWRWNAEWUGWESAGQMIBFGWMSZSKBXNBMZPMOQWUCZIGTKQTNXWKVBG
# USGBHEEJBAAUZSGJNTGGKMTLYQYWNLGZBVZSHHRWNNRWWIVOZHNBXRCSNTXHEDBK
# AISQHCYIAVMPTTLGNZXSCWGLBNTSEUHSGSETROHJMQFEBFMPXOEQLBTRGLNZGIAY
# LWFENLMMGTVGGBHPESVBBCNDMPBNTKBBPIYDBUIRBNXGHUELAMHRVWLQYYBMYQGD
# GZTBROHJXAIEAVBVZAYEHAMAYDRWNRGAFMHNCJTKMIPWLBTRGLNZGIAYLWFENLMM
# GTVGGBHTUWHZXTVUTTMHVFZABTJAETBMCJHDXYBMKXKAPLBKXDBFTTWKAMMP
#
##############################################
from collections import Counter
import string
ciphertext = "BNWEOMZOBNTALBAECJHKXSFGYZXMBNBVZSBXMETRRTNOLTUWGXKOTJTUFIAYFCLTOWMPXPEGVMLSBXICMTVFZBAEZAGMWSTWKLBJXKMZTDRTNOZIAYBAMWVUXILHNJWILWEAMQGGGZXKHDRAGBAESAKAMPYSVMMHRJXNHRRAYGHUJJBBXTUWVWWENKVTXVRJEGTSCGLABBYWRWNAEWUGWESAGQMIBFGWMSZSKBXNBMZPMOQWUCZIGTKQTNXWKVBGUSGBHEEJBAAUZSGJNTGGKMTLYQYWNLGZBVZSHHRWNNRWWIVOZHNBXRCSNTXHEDBKAISQHCYIAVMPTTLGNZXSCWGLBNTSEUHSGSETROHJMQFEBFMPXOEQLBTRGLNZGIAYLWFENLMMGTVGGBHPESVBBCNDMPBNTKBBPIYDBUIRBNXGHUELAMHRVWLQYYBMYQGDGZTBROHJXAIEAVBVZAYEHAMAYDRWNRGAFMHNCJTKMIPWLBTRGLNZGIAYLWFENLMMGTVGGBHTUWHZXTVUTTMHVFZABTJAETBMCJHDXYBMKXKAPLBKXDBFTTWKAMMP"

# English letter frequency probabilities (from Table 2.1)
english_letter_probabilities = {
    'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127, 'F': 0.022,
    'G': 0.02,  'H': 0.061, 'I': 0.07,  'J': 0.002, 'K': 0.008, 'L': 0.04,
    'M': 0.024, 'N': 0.067, 'O': 0.075, 'P': 0.019, 'Q': 0.001, 'R': 0.06,
    'S': 0.063, 'T': 0.091, 'U': 0.028, 'V': 0.01, 'W': 0.023, 'X': 0.001,
    'Y': 0.02, 'Z': 0.001
}

alphabet = string.ascii_uppercase
key_length = 6
substrings = ['' for _ in range(key_length)]

# Step 1: Split ciphertext into 6 substrings
for index, char in enumerate(ciphertext):
    substrings[index % key_length] += char

# Step 2: Analyze each substring to find most likely shift
keyword = ""

for idx, substring in enumerate(substrings):
    substring_length = len(substring)
    mg_scores = []

    for shift in range(26):
        # Decrypt with Caesar shift
        decrypted_chars = [
            alphabet[(alphabet.index(char) - shift) % 26] for char in substring
        ]
        decrypted_string = ''.join(decrypted_chars)

        # Frequency count
        letter_counts = Counter(decrypted_string)

        # Calculate Mg
        mg = sum(
            (letter_counts.get(letter, 0) * english_letter_probabilities[letter]) / substring_length
            for letter in alphabet
        )
        mg_scores.append((shift, mg))

    # Optional: print results for this substring
    string = ""
    for shift, mg in mg_scores:
        string += f"{mg:.3f}\t"
    print(string)

plaintext_chars = []
key_shifts = [19, 8, 19, 0, 13, 18] 
for idx, char in enumerate(ciphertext):
    # Convert 'A'..'Z' → 0..25
    cipher_val = ord(char) - ord('A')
    # Subtract the key shift, wrap mod 26
    plain_val = (cipher_val - key_shifts[idx % key_length]) % 26
    # Convert back to 'A'..'Z'
    plaintext_chars.append(chr(plain_val + ord('A')))


print("".join(plaintext_chars))
