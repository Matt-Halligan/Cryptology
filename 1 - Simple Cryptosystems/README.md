# Project 1 - Simple Cryptosystems

## Project Overview

This assignment demonstrates core introductory cryptanalysis techniques through the implementation of three standalone Python scripts:

	•	Vigenère Cipher Decryptor — recovers the plaintext of a long ciphertext using frequency analysis using the Mg score assuming a known key length.

	•	Caesar Cipher Brute-Force Decryptor — performs exhaustive search of all 26 possible shifts.

	•	Permutation Cipher Decryptor — decrypts a block-transposition cipher using an inverse of the given permutation key.

These programs emphasize classical cryptosystem weaknesses, cryptanalytic methods, and Python implementation of the techniques discussed in class.

## Program Descriptions

1. Vigenère Cipher Decryption via Frequency Analysis

- This script decrypts a long Vigenère-encrypted ciphertext using:
	•	Known key length (6)

	•	English letter probability distribution

	•	Mg scoring across all 26 possible shifts for each substring

	•	Derivation of most likely key shifts

	•	Full plaintext reconstruction

2. Caesar Cipher Exhaustive Key Search

- This script brute-forces all 26 Caesar-shift keys for ciphertext.

3. Permutation Cipher Decryption for Block Size m = 9

- This script decrypts a permutation cipher using the permutation key

π = [9, 5, 3, 2, 1, 7, 4, 6, 8]