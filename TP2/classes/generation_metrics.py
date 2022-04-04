class GenerationMetrics:
    def __init__(self, generation_number,  population ):
        self.generation_number = generation_number
        self.mean_fitness = mean_fitness(population)
        self.max_fitness = max_fitness(population)
        self.min_fitness = min_fitness(population)
    
    def __str__(self):
        return f"nr: {self.generation_number} max: {self.max_fitness} min: {self.min_fitness} error: {3-self.mean_fitness} mean:{self.mean_fitness}"

    def __repr__(self):
        return f"nr: {self.generation_number} max: {self.max_fitness} min: {self.min_fitness} error: {3-self.mean_fitness} mean:{self.mean_fitness}"

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