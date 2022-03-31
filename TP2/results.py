import time

from matplotlib import pyplot as plt
from classes.generation_metrics import GenerationMetrics
from config_parser import import_config
from functions import match_genotypes
from solver import create_initial_population


def main():
    CONFIG_FILE = 'config.json'
    # parseo el input
    config = import_config(CONFIG_FILE)
    # generar población inicial
    initial_population = create_initial_population(config.reagents, config.exact_values)
    # sacar del config parseado la cantidad de iteraciones
    execution_count = 0
    starttime = time.time()
    generation_metrics = dict()
    # iterar
    while execution_count <= config.execution_count:
        generation_metrics[execution_count] = []
        generation_count = 0
        current_gen_metrics = GenerationMetrics(generation_count, initial_population)
        generation_metrics[execution_count].append(current_gen_metrics)
        current_population = initial_population
        while config.break_condition.checkBreak(time.time() - starttime, current_gen_metrics):
            new_population = []
            new_population_size = 0
            i = 0
            parents = match_genotypes(current_population)
            while new_population_size < config.population_size:
                # cruza
                child_1, child_2 = config.cross_method.cross(parents[i][0], parents[i][1])

                # mutacion
                m_child_1 = config.mutation.mutate(child_1)
                m_child_2 = config.mutation.mutate(child_2)

                # agrego mutaciones ala poblacion nueva
                new_population.extend([m_child_1, m_child_2])
                new_population_size +=2

                # incremento indice de padres
                i+=1
            # selección
            current_population = config.selection.select(current_population + new_population, config.population_size)
            generation_count +=1
            # calculo las métricas de generacion
            generation_metrics[execution_count].append(GenerationMetrics(generation_count, current_population))
        execution_count += 1
    



def create_graph(generation, mean_fitness, max_fitness, min_fitness, gen_diveristy, fitness_diversity, gen_breach):
    figure, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(3, 3)

    ax1.set_xlabel('Número de generación')
    ax1.set_ylabel('Fitness promedio')
    ax1.plot(generation, mean_fitness)

    ax2.set_xlabel('Número de generación')
    ax2.set_ylabel('Máximo fitness')
    ax2.plot(generation, max_fitness)

    ax3.set_xlabel('Número de generación')
    ax3.set_ylabel('Mínimo fitness')
    ax3.plot(generation, min_fitness)

    ax4.set_xlabel('Número de generación')
    ax4.set_ylabel('Diversidad de genes')
    ax1.plot(generation, gen_diveristy)

    ax5.set_xlabel('Número de generación')
    ax5.set_ylabel('Diversidad de fitness')
    ax1.plot(generation, fitness_diversity)

    ax6.set_xlabel('Número de generación')
    ax6.set_ylabel('Brecha generacional')
    ax1.plot(generation, gen_breach)


    plt.savefig('/output/')
    plt.show()
