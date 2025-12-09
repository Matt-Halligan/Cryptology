# Project 6 - Other Public Key Systems

## Project Overview
This project implements classical number-theoretic algorithms used in cryptography, focusing on discrete logarithms in finite fields and decryption using the ElGamal scheme. The implementations are educational and explicit, using only Python’s built-in capabilities. The project contains two main pieces:

Shank's Baby-step Giant-step discrete logarithm algorithm — computes discrete logarithms efficiently using the square-root decomposition method.

ElGamal decryption — decrypts ciphertext pairs (c1,c2) using a recovered private key and modular arithmetic.

## Program Descriptions

1. Shanks.py

- This script: 

	• Finds the discrete logarithm for a given number, modulo a prime.
	
	• Uses a standard algorithm that splits the work into two parts, computes lists of numbers, and searches for a match.
	
	• Output: prints the secret exponent.

2. ElGamal.py

- This script:

	• Recovers the private key by checking powers of a known base until it matches the public key.

	• Reads ciphertext pairs and calculates the original message using modular arithmetic.

	• Converts numeric message blocks back into letters.

	• Output: prints the fully decrypted plaintext message.
