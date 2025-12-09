# Cryptology

This repository contains a collection of Python-based cryptography projects completed as part of graduate coursework in Cryptology Summer 2025. Each subproject explores a distinct area of cryptography, including classical ciphers, block ciphers, public key systems, discrete logarithms, elliptic curve cryptography, and digital signatures.

The projects are educational and designed to demonstrate core cryptographic principles through explicit Python implementations without relying on external libraries. They cover both analysis and attacks on cryptosystems as well as secure constructions of cryptographic schemes.

## Projects

1. Simple Cryptosystems
Implements classical cryptanalysis techniques including Vigenère, Caesar, and permutation ciphers.

	•	Decrypts ciphertexts using frequency analysis and exhaustive search.

	•	Explores weaknesses of early cryptographic systems.

2. Block Ciphers
Demonstrates AES key expansion, showing how round keys are derived from a cipher key.

	•	Implements the full AES-128 key schedule in Python.

	•	Outputs all round keys for educational inspection.

3. Block Cipher Attacks
Explores S-box analysis for linear and differential cryptanalysis.

	•	Constructs tables showing how input differences and linear masks affect output.

	•	Provides insight into potential vulnerabilities in block ciphers.

4. Public Key Cryptosystems
Focuses on foundational number-theoretic algorithms used in public key cryptography.

	•	Implements modular exponentiation, extended Euclidean algorithm, and the Chinese Remainder Theorem.

	•	Demonstrates RSA-related computations like decryption and solving modular systems.

5. RSA Cryptosystem Attacks
Provides hands-on attacks and factoring methods relevant to RSA.

	•	Brute-forces small plaintext blocks using exponentiation.

	•	Implements Pollard’s rho and Dixon’s method to factor integers.

	•	Includes solving modular systems with CRT.

6. Other Public Key Systems
Covers discrete logarithms and ElGamal decryption.

	•	Implements Shank’s Baby-Step Giant-Step algorithm for computing discrete logs.

	•	Decrypts ElGamal ciphertext using recovered private keys and modular arithmetic.

7. Discrete Logs and Elliptic Curves
Explores elliptic curve cryptography with small parameters.

	•	Decrypts messages encoded on an elliptic curve.

	•	Searches for private keys by brute-force point multiplication.

	•	Highlights practical differences between finite field and elliptic curve computations.

8. Signature Schemes
Implements both classical DSA and elliptic curve DSA.

	•	Generates digital signatures and verifies authenticity.

	•	Demonstrates public key computation from private keys on elliptic curves.

	•	Provides a complete workflow for signing and verification of messages.

These projects collectively demonstrate the principles of cryptanalysis, public key cryptography, discrete logarithms, elliptic curve operations, and digital signatures. They serve as a comprehensive educational resource for students exploring cryptographic systems, attacks, and secure constructions.