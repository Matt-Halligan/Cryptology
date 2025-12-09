# Project 5 - RSA Cryptosystem Attacks

## Project Overview
This project implements a collection of classical number-theoretic algorithms used in cryptography and computational number theory. The implementations are intentionally explicit and educational with no external libraries required for functionality. The project contains four main pieces:

•	On-the-fly decoder using Square-and-Multiply exponentiation — brute-forces 3-letter plaintext blocks by inverting base^e mod m for a fixed exponent and modulus.

•	Pollard’s rho factorization — probabilistic algorithm to find a nontrivial factor of a composite integer.

•	Dixon’s method scan — small B-smooth search for z values over a range to demonstrate quadratic residue relations useful for Dixon’s factoring.

•	Chinese Remainder Theorem (CRT) solver — standard construction to solve a system of pairwise-coprime congruences.

## Program Descriptions

1. Square_and_Multiply_Algorithm.py
- This script:

	•	Uses the efficient square-and-multiply (binary exponentiation) method implemented in modular_exponentiation(base, exponent, modulus).

	•	decode(exponent, modulus, block) brute-forces all 26³ possible 3-letter combinations and returns the matching plaintext block when base^exponent mod modulus == block.

	•	The provided script runs the decoder on five large ciphertext block_i values and concatenates the recovered blocks into the final decoded string.

	•	Output: prints each recovered 3-letter block and the final decoded string.

2. Pollards_Rho.py

- This script:

	•	Implements polynomial iteration f(x) = x^2 + c (mod n) with parameters x1 (seed) and c (constant).

	•	Uses Floyd’s cycle detection (x and x′ = f(f(x))) and computes gcd(|x-x′|, n).

	•	Loop runs until a nontrivial factor is found or a failure condition (p == n) occurs (which suggests retry with different x1/c).

	•	Output: prints found factor, cofactor, and iteration count.

3. Dixons_Random_Squares_Algorithm.py

- This script:

	•	The factor base B is provided as [-1, 2, 3, 5, 7, 11, 13, 17, 19, 23] (negative one used to track sign).

	•	For each z in the chosen range (example: 600..660), compute original = (n - z^2) and attempt to factor original over B.

	•	If original becomes 1 (fully factored), the exponent vector over B is recorded (this vector would be useful in the linear algebra step of Dixon’s algorithm).

	•	Output: prints z, the factorization, and the exponent vector when a successful factorization is found.

4. Chinese_Remainder_Theorem_Algorithm.py

- This script:

	•	Computes total modulus M = ∏ m_i.

	•	For each congruence, computes partial product M_i = M / m_i and modular inverse y_i = M_i^{-1} mod m_i with pow(M_i, -1, m_i).

	•	Accumulates solution x = Σ a_i * M_i * y_i and reduces x mod M.

	•	Output: prints M and the solved x.