class GenerationMetrics:
    def __init__(self, generation_number,  population, fixed_fitness,last_best_solutions, last_diversities):
        self.generation_number = generation_number
        self.mean_fitness = mean_fitness(population)
        self.max_fitness = max_fitness(population)
        self.min_fitness = min_fitness(population)
        self.gen_diversity = invididuals_diversity(population)
        self.fit_diversity = fitness_diversity_with_precision(population)
        self.fixed_fitness = fixed_fitness
        self.last_best_solutions = insert_last_solutions(fixed_fitness, self.max_fitness, last_best_solutions)
        self.last_diversities = insert_last_diversities(fixed_fitness, self.gen_diversity, last_diversities)
    
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

def insert_last_solutions(fixed_fitness, max_fitness, last_best_solutions):
    
    if len(last_best_solutions) == fixed_fitness:
        last_best_solutions.popleft()
    last_best_solutions.append(max_fitness)
    return last_best_solutions
    
def insert_last_diversities(fixed_fitness, gen_diversity, last_diversities):
    
    if len(last_diversities) == fixed_fitness:
        last_diversities.popleft()
    last_diversities.append(gen_diversity)
    #print(last_diversities)
    return last_diversities

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


