class GenerationMetrics:
    def __init__(self, generation_number,  population ):
        self.generation_number = generation_number
        self.mean_fitness = mean_fitness(population)
        self.max_fitness = max_fitness(population)
        self.min_fitness = min_fitness(population)

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