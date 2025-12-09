# Project 7 - Discrete Logs and Elliptic Curves

## Project Overview

This project explores simple elliptic curve cryptography operations in Python. It focuses on two main tasks: decrypting messages and finding private keys using brute-force search. The implementations are educational and avoid external libraries. The project contains two main scripts:

•	Elliptic Curve Decryption — recovers plaintext messages from elliptic curve ciphertext.

•	Elliptic Curve Private Key Search — finds the private key that relates two points on an elliptic curve.

## Program Descriptions

1. simple_elliptic_curve_decryption.py - Elliptic Curve Decryption
- This script:

	• Uses modular arithmetic to handle calculations over a finite field.

	• Reconstructs full points from compressed coordinates using a parity bit.

	• Adds points repeatedly to simulate scalar multiplication on the elliptic curve.

	• Computes the original message from the ciphertext and converts numeric values into letters.

	• Output: prints the numeric decoded message and the final plaintext string.


2.  private_key_searcher.py - Elliptic Curve Private Key Search
- This script:

	• Searches for the private key by repeatedly adding a known point to itself until the result matches a target point.

	• Implements elliptic curve point addition rules including doubling and inverse cases.
	
	• Stops once the matching multiple is found or a maximum search limit is reached.
	
	• Output: prints the private key if found, or a message indicating no key was found within the search limit.