##############################################
# Matthew Halligan
# Cryptology Summer 2025
# Module 11 Assignment 11, Question 1
# Professor Tom McGuire
#
# Digital Signature Algorithm
#
# Referenced from DSA.ipynb course material 
# modified to fit assignment instructions
#
##############################################
def hash(z):
    return 52

q = 101
p=7879
a = 75
alpha = 170
beta = pow(alpha, a, p)
k=49

x=52

k_inv = pow(k, -1, q)
gamma = pow(alpha, k, p) %q
delta = ((hash(x) + a*gamma)*k_inv) % q

sig = (gamma, delta)

print(f"Given these parameters:\n\tq =\t{q}\n\tp=\t{p}\n\ta =\t{a}\n\talpha =\t{alpha}\n\tbeta =\t{beta}\n\tk =\t{k}\n\tk_inv =\t{k_inv}\n\tgamma =\t{gamma}\n\tdelta =\t{delta}")

print(f"Signature for {x} is {sig}")

e1 = (hash(x)*pow(delta, -1, q)) % q
e2 = (gamma*pow(delta, -1, q)) % q

ver = (((pow(alpha, e1, p)*pow(beta, e2, p))%p) %q) ==gamma
print(ver)
       


