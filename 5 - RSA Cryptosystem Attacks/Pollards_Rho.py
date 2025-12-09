##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 8 Assignment 8, question 3
# Professor Tom McGuire
#
# Pollard's rho factoring algorithm
# Attempt to find a nontrivial factor of n using Pollard's rho.
#   n     integer to factor
#   x1    initial seed (random if None)
#   c     constant term for f (random in [1, n-1] if None)
#   outputs a factor p (1 < p < n) or failure message on failure
##############################################

import random
from math import gcd

def f(x, c, n):
    return (x * x + c) % n

n=53081719
n=44818676050679
n=146909665438467220848264259950499
x1=31
c=1
factor = None
iterations=0


if n % 2 == 0:
    factor = 2

x = x1
x_prime = f(x, c, n)
p = gcd(abs(x - x_prime), n)

# iterate until finding a factor or declare failure
while p == 1:
    # in the i'th iteration, x = x_i and x_prime = x_{2i}
    x = f(x, c, n)
    x_prime = f(f(x_prime, c, n), c, n)
    p = gcd(abs(x - x_prime), n)
    iterations += 1

if p == n:
    # retry with different parameters
    factor = "Not found"
else:
    factor = p
    
print(f"Completely factoring: {n}")
print(f"parameters: [x1={x1}, c={c}]")
if factor != "Not Found":
    print(f"\tFound factor: {factor}")
    print(f"\tCo-factor: {n // factor}")
    print(f"\tIterations to factor: {iterations}")
else:
    print("Factors not found. failure")
