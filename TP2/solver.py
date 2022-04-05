
from results import generate_graph
from utils.generate_csv import average_csv_files, generate_csv_file
from classes.genotype import Individual
import random 
import sys
import numpy as np
from functions import match_genotypes
from classes.population import Population
from interfaces.cross import SimpleCross
from interfaces.mutations import UniformMutation
from interfaces.selection import EliteSelection
import time

from classes.generation_metrics import GenerationMetrics
import config_parser
from functions import match_genotypes

def create_initial_population(sigma,exact_values, pop_size):
    individuals = []
    for i in range(pop_size):
        # sys.maxsize
        values = []
        for n in range(11):
            #values.append(random.uniform(-sys.maxsize,sys.maxsize))
            values.append(random.uniform(-10,10))
        
        W = values[:3]
        omega = values[3:9]
        omega_zero = values[9:11]
        genotype = Individual(values,exact_values, sigma)
        
        individuals.append(genotype)
        


    return individuals

def main():
    config_file_path = 'config.json'
    # parseo el input
    config_parser.initialize_config(config_file_path)
    # generar población inicial
    # for p in initial_population:
        # print(p.fitness)
    
    # sacar del config parseado la cantidad de iteraciones
 
   
    variation_count = 0
    # iterar
    
    while variation_count < config_parser.config.execution_variants:
        initial_population = create_initial_population(config_parser.config.reagents, config_parser.config.exact_values, config_parser.config.population_size)
        execution_count = 0
        generation_metrics = dict()
        while execution_count < config_parser.config.execution_count:
            starttime = time.time()            
            generation_metrics[execution_count] = []
            generation_count = 0
            current_gen_metrics = GenerationMetrics(generation_count, initial_population)
            generation_metrics[execution_count].append(current_gen_metrics)
            current_population = initial_population
            
            while not config_parser.config.break_condition.checkBreak(time.time() - starttime, current_gen_metrics):
            #while generation_count < 500:
                new_population = []
                new_population_size = 0
                i = 0
                parents = config_parser.config.parent_selection_method.select(current_population)
                while new_population_size < config_parser.config.population_size:
                    # cruza
                    child_1, child_2 = config_parser.config.cross_method.cross(parents[i][0], parents[i][1])

                    # mutacion
                    m_child_1 = config_parser.config.mutation.mutate(child_1)
                    m_child_2 = config_parser.config.mutation.mutate(child_2)

                    # agrego mutaciones ala poblacion nueva
                    new_population.extend([m_child_1, m_child_2])
                    new_population_size +=2

                    # incremento indice de padres
                    i+=1
                # selección
                if config_parser.config.selection.method_name == 'boltzmann':
                    current_population = config_parser.config.selection.select(current_population + new_population, config_parser.config.population_size,generation_count+1)
                else:
                    current_population = config_parser.config.selection.select(current_population + new_population, config_parser.config.population_size)
                generation_count +=1
                # calculo las métricas de generacion
                a  = GenerationMetrics(generation_count, current_population)
                current_gen_metrics = a
                generation_metrics[execution_count].append(a)
            file_base = f"{config_parser.config.selection.method_name}_{config_parser.config.break_condition.method_name}_{config_parser.config.cross_method.method_name}_{config_parser.config.mutation.method_name}"
            generate_csv_file(f"output/raw/{variation_count}_{file_base}_{execution_count}.csv", generation_metrics[execution_count])
            execution_count += 1
        average_csv_files(f"{variation_count}_{file_base}", config_parser.config.execution_count, config_parser.config.break_condition.generation_count)
        variation_count+=1
    generate_graph(file_base, config_parser.config.execution_variants)


# P: int = 100





# def solve():
#     # Receive sigma from input

#     ## Temporarily Hardcoded ##
#     sigma = [[0 for _ in range(3)] for _ in range(3)]
#     sigma[0][0] = 4.4793
#     sigma[0][1] = -4.0765
#     sigma[0][2] = -4.0765

#     sigma[1][0] = -4.1793
#     sigma[1][1] = -4.9218
#     sigma[1][2] = 1.7664

#     sigma[2][0] = -3.9429
#     sigma[2][1] = -0.7689
#     sigma[2][2] = 4.8830

#     exact_values = [0,1,1]


#     # Create initial population (quantity P) con numero par de indiv. 
#     current_population = create_initial_population(sigma,exact_values)
#     generation_count = 0
#     genetic_cross = SimpleCross()
#     genetic_mutation = UniformMutation()
#     genetic_selection = EliteSelection()
#     # while (condicion corte)
#     while generation_count <= 500:
#         # Create new empty population
#         new_population = []
#         # while new population size < 2P
#         parents = match_genotypes(current_population)
#         print(len(current_population))
#         print('Parent len : {}'.format(len(parents)))
#         i=0
#         while len(new_population) < 2*P:
#             # seleccionar 2 individuos
#             print('I:{}'.format(i))
#             print('new population {}'.format(len(new_population)))
#             # Cruzar los 2 individuos
#             child_1, child_2 = genetic_cross.cross(parents[i][0], parents[i][1])
#             # Mutacion de nuevos individuos
#             m_child_1 = genetic_mutation.mutate(child_1)
#             m_child_2 = genetic_mutation.mutate(child_2)


#             new_population.extend([parents[i][0], parents[i][1], m_child_1, m_child_2])
#             i+=1
#         # Seleccion de individuos
#         new_population = genetic_selection.select(new_population, P)
        
#         # Intercambio de poblaciones
#         current_population = new_population
#         generation_count+=1


if __name__ == '__main__':
    main()