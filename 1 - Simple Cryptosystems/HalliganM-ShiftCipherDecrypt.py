##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 1 Assignment 1
# Professor Tom McGuire
#
# Use an exhaustive key search to decrypt the following cipher text 
# XQFETMHQEAYQRGZIUFTODKBFAMFVTG
#
##############################################


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "XQFETMHQEAYQRGZIUFTODKBFAMFVTG"

for shift_key in range(26):
    plaintext = ''
    for char in cipher:
        index = alphabet.index(char)
        shifted_index = (index - shift_key) % 26
        plaintext += alphabet[shifted_index]
    print(f"Key={shift_key}: {plaintext}")
        
