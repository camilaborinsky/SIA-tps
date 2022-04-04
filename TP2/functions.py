from operator import ge
import numpy as np 
import math
import random

def g(x):
    try:
        return math.exp(x) / (1 + math.exp(x))
    except:
        return 1

def big_f(W, omega, omega_zero, sigma):
    # print("Omega zero")
    # print(omega_zero)
    outside_sum : float = 0
    for j in range(0,2):
        inside_sum = 0
        for k in range(0,3):
            inside_sum += float(omega[j*3+k]) * float(sigma[k])
        inside_sum -= omega_zero[j]  #TODO: preguntar si es con omega_zero
        inside_g = g(inside_sum)
        outside_sum += inside_g * W[j+1] #TODO: preguntar si es con j+1
    outside_g = g(outside_sum- W[0])
    # print("Outside {}".format(outside_g))
    return outside_g

            
        

def error(W, omega, omega_zero, exact_values,sigma_list):
    
    error: float = 0
    for i in range(0,3):
        error += pow(exact_values[i]-big_f(W, omega, omega_zero,sigma_list[i]),2)
    # print("Error: {}".format(error))
    return error

def match_genotypes (genotypes):
    targets = list(genotypes)

    random.shuffle(targets)
    return list(zip(genotypes, targets))



