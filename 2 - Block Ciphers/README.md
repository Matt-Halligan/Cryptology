# Project 2 - Block Ciphers

## Project Overview

This project implements the AES-128 key expansion algorithm to compute all 11 round keys (K[0]–K[10]) from an initial 128-bit cipher key. The implementation follows Algorithm 4.6 from Cryptography: Theory and Practice (Stinson, 4th Edition) and demonstrates the inner mechanics of AES key scheduling, including byte substitution, word rotation, XOR operations, and Rcon integration.

The script outputs each round key in hexadecimal and organizes the results in a pandas DataFrame for readability.

## Program Descriptions

1. AES-KeySchedule.py
- This script computes the full AES-128 round key schedule.


## References 
•	Douglas R. Stinson, Cryptography: Theory and Practice, 4th Edition