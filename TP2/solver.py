
from classes.genotype import Individual
import random 
import sys
import numpy as np
from functions import match_genotypes
from classes.population import Population
from interfaces.cross import SimpleCross
from interfaces.mutations import UniformMutation
from interfaces.selection import EliteSelection


P: int = 100



def create_initial_population(sigma,exact_values):
    individuals = []
    for i in range(P):
        # sys.maxsize
        values = []
        for n in range(11):
            #values.append(random.uniform(-sys.maxsize,sys.maxsize))
            values.append(random.uniform(-100,100))
        
        W = values[:3]
        omega = values[3:9]
        omega_zero = values[9:11]
        genotype = Individual(values,exact_values, sigma)
        
        individuals.append(genotype)
        


    return individuals

def solve():
    # Receive sigma from input

    ## Temporarily Hardcoded ##
    sigma = [[0 for _ in range(3)] for _ in range(3)]
    sigma[0][0] = 4.4793
    sigma[0][1] = -4.0765
    sigma[0][2] = -4.0765

    sigma[1][0] = -4.1793
    sigma[1][1] = -4.9218
    sigma[1][2] = 1.7664

    sigma[2][0] = -3.9429
    sigma[2][1] = -0.7689
    sigma[2][2] = 4.8830

    exact_values = [0,1,1]


    # Create initial population (quantity P) con numero par de indiv. 
    current_population = create_initial_population(sigma,exact_values)
    generation_count = 0
    genetic_cross = SimpleCross()
    genetic_mutation = UniformMutation()
    genetic_selection = EliteSelection()
    # while (condicion corte)
    while generation_count <= 500:
        # Create new empty population
        new_population = []
        # while new population size < 2P
        parents = match_genotypes(current_population)
        print(len(current_population))
        print('Parent len : {}'.format(len(parents)))
        i=0
        while len(new_population) < 2*P:
            # seleccionar 2 individuos
            print('I:{}'.format(i))
            print('new population {}'.format(len(new_population)))
            # Cruzar los 2 individuos
            child_1, child_2 = genetic_cross.cross(parents[i][0], parents[i][1])
            # Mutacion de nuevos individuos
            m_child_1 = genetic_mutation.mutate(child_1)
            m_child_2 = genetic_mutation.mutate(child_2)


            new_population.extend([parents[i][0], parents[i][1], m_child_1, m_child_2])
            i+=1
        # Seleccion de individuos
        new_population = genetic_selection.select(new_population, P)
        
        # Intercambio de poblaciones
        current_population = new_population
        generation_count+=1


if __name__ == '__main__':
    solve()