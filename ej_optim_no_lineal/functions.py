import math


def g(x):
    try:
        return math.exp(x) / (1 + math.exp(x))
    except:
        return 1

def f(W, omega, omega_zero, sigma):
    outside_sum : float = 0
    for j in range(0,2):
        inside_sum = 0
        for k in range(0,3):
            inside_sum += float(omega[j*3+k]) * float(sigma[k])
        inside_sum -= omega_zero[j] 
        inside_g = g(inside_sum)
        outside_sum += inside_g * W[j+1] 
    outside_g = g(outside_sum- W[0])
    return outside_g

def error(genotype, exact_values,sigma_list):   
    W = genotype[0:3]
    omega = genotype[3:9]
    omega_zero = genotype[9:11]
    error: float = 0
    for i in range(0,3):
        error += pow(exact_values[i]-f(W, omega, omega_zero,sigma_list[i]),2)
    return error

class ErrorWrapper:
    def __init__(self, reagents, expected_output):
        self.reagents = reagents
        self.expected_output = expected_output
    
    def apply_function(self, genotypes, step=None):
        return error(genotypes, self.expected_output, self.reagents)