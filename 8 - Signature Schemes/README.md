# Project 8 - Signature Schemes

## Project Overview
This project implements digital signature algorithms using both classical DSA and elliptic curve cryptography. It focuses on signing messages and verifying signatures, as well as computing public keys on elliptic curves. The implementations are explicit and educational, avoiding external libraries. The project contains three main scripts:

•	DSA Signature — generates and verifies classical digital signatures using DSA parameters.

•	Elliptic Curve DSA (ECDSA) — computes signatures for messages using elliptic curve arithmetic and verifies them.

•	Elliptic Curve Public Key Calculator — computes a public key from a private key by scalar multiplication on an elliptic curve.

## Program Descriptions

1. DSA.py
- This script:

	• Defines a simple hash function for the message.

	• Computes the signature (gamma, delta) for a message using DSA parameters.

	• Verifies the signature by reconstructing the expected value from the signature components.

	• Output: prints all intermediate values, the generated signature, and verification result i.e., True/False.

2. ECDSA.py

- This script:

	• Implements point addition and scalar multiplication on a small elliptic curve.

	• Computes a public key B = m·A from a private key m.

	• Signs a message using an ephemeral key k, producing a signature (r, s).

	• Verifies the signature by recomputing the point on the curve and checking if it matches r.

	• Output: prints the signature and whether verification succeeds i.e., True/False.

3. ECDSA-public key calculator.py

- This script:

	• Performs repeated addition of a generator point to compute the public key B = m·A.

	• Implements the same point addition rules used in ECDSA including doubling and inverses.

	• Output: prints the resulting public key point B.