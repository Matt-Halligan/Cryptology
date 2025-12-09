# Project 3 - Block Cipher Attacks

## Project Overview
This project computes two fundamental tables used in block-cipher analysis:

Linear Approximation Table (LAT) 
Differential Distribution Table (DDT) 	​

These tables describe how an S-box behaves under linear and differential cryptanalysis.

## Program Descriptions

1. Linear Approximation Table - "N_L Table Calculator.py"

- This script:

•	Defines the S-box.

•	Implements inner_prod() to compute the binary parity of masked inputs.

•	Iterates over all a,b,x∈[0,15].

•	Populates a 16×16 LAT.

•	Prints the table in a tabular format.

The resulting table allows analysis of linear biases in the S-box, which indicates which linear approximations may be useful in linear cryptanalysis.

2. Differential Distribution Table - "N_D Table Calculator.py"

- This script:

•	Defines the S-box for question 2.

•	Initializes a 16×16 differential distribution table.

•	For every input difference u', evaluates all z∈[0,15].

•	Computes the corresponding output difference v'.

•	Counts occurrences of each (u′,v′) pair.

•	Prints the table in row-by-row form.

This table is used to measure how predictably differences propagate through the S-box, a critical factor for differential cryptanalysis.

