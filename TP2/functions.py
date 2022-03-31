from operator import ge
from math import exp
import numpy as np 
import random

def g(x):
    return np.exp(x)/(1+np.exp(x))

def big_f(W, omega, omega_zero, sigma):
    outside_sum = 0
    inside_sum = 0
    for j in range(0,1):
        for k in range(0,2):
            inside_sum += omega[j*3+k] * sigma[k]
            inside_sum -= omega_zero[j]  #TODO: preguntar si es con omega_zero
        inside_g = g(inside_sum)
        outside_sum += inside_g * W[j+1] #TODO: preguntar si es con j+1
    outside_g = g(outside_sum- W[0])
    return outside_g

            
        

def error(W, omega, omega_zero, exact_values,sigma_list):
    error: float = 0
    
    for i in range(0,2):
        error += pow(exact_values[i]-big_f(W, omega, omega_zero,sigma_list),2)

    return error

def match_genotypes (genotypes):
    targets = list(genotypes)

    random.shuffle(targets)
    return list(zip(genotypes, targets))

def mean_fitness(population):
    return sum(list(map(lambda individual: individual.fitness, population)))/len(population)

def min_fitness(population):
    return min(list(map(lambda individual: individual.fitness, population)))

def max_fitness(population):
    return max(list(map(lambda individual: individual.fitness, population)))

def fitness_diversity(population):
    fitness_unique_values = 0
    # for i in enumerate(population):
    #     for j in enumerate(population):
    #         if(abs(i.fitness - j.fitness) > PRECISION ):


