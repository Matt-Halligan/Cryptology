# Project 4 - Public Key Cryptosystems

## Project Overview

This project implements three fundamental number-theoretic algorithms used throughout modern public-key cryptography:

1. Modular Exponentiation (Square-and-Multiply)

2. Extended Euclidean Algorithm (Multiplicative Inverses)

3. Chinese Remainder Theorem (CRT) Solver

The code examples are written in Python and designed to work without third-party libraries.

## Program Descriptions

1. Modular Exponentiation (Square-and-Multiply)

* This script:

	•	Allows selecting different bases by uncommenting one of the assignments.

	•	Uses a fixed exponent of 65537 (the common RSA public exponent).

	•	Computes and prints the result with the square-and-multiply method.

2. Extended Euclidean Algorithm (Multiplicative Inverses)

* This script:

	•	Allows selecting from multiple (a, b) pairs by uncommenting lines.

	•	Runs a manual, iterative implementation of the Extended Euclidean Algorithm.

3. Chinese Remainder Theorem (CRT) Solver

* This script:

	•	Defines a list of moduli and corresponding remainders.

	•	Computes the full product M.

	•	Uses Python’s built-in pow(Mi, -1, mi) to compute inverses.

	•	Produces the unique solution modulo M.

CRT is widely used for speeding up RSA decryption and signing.
