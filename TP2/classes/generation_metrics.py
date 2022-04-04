class GenerationMetrics:
    def __init__(self, generation_number,  population ):
        self.generation_number = generation_number
        self.mean_fitness = mean_fitness(population)
        self.max_fitness = max_fitness(population)
        self.min_fitness = min_fitness(population)
    
    def __str__(self):
        return f"nr: {self.generation_number} max: {self.max_fitness} min: {self.min_fitness} mean:{self.mean_fitness}"

    def __repr__(self):
        return f"nr: {self.generation_number} max: {self.max_fitness} min: {self.min_fitness} mean:{self.mean_fitness}"

def mean_fitness(population):
    return sum(list(map(lambda individual: individual.fitness, population)))/len(population)

def min_fitness(population):
    return min(list(map(lambda individual: individual.fitness, population)))

def max_fitness(population):
    return max(list(map(lambda individual: individual.fitness, population)))


def invididuals_diversity(population):
    #Create set with genotypes of all individuals
    genotypes = set()
    for individual in population:
        genotypes.add(individual)
    total_genotypes = len(genotypes)
    return total_genotypes/len(population)

def exact_fitness_diversity(population):
    #Create set with fitnesses of all individuals
    fitnesses = set()
    for individual in population:
        fitnesses.add(individual.fitness)
    total_fitnesses = len(fitnesses)
    return total_fitnesses/len(population)

def fitness_diversity_with_precision(population):
    #Chequeo todos los individuos del i hacia adelante a ver si alguno es "igual" que el current, si no hay ninguno incremento diversity. 
    length = len(population)
    diversity = 0
    for i in range(0, length):
        matched = False
        for j in range (i+1, length):
            if abs(population[i].fitness - population[j].fitness) > 0.00001: #FIXME change value to precision from input
                matched = True
        if not matched:
            diversity += 1
    return diversity/len(population)


