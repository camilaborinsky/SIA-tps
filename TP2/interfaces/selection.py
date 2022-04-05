import copy
import random
from numpy import exp





class Selection:
    def select(self, population, pop_size):
        return population
    
    def __init__ (self, method_name):
        self.method_name = method_name

class StochasticSelection(Selection):
    def select(self, population, pop_size, prob):
        return population

class EliteSelection(Selection):
    def select(self, population, pop_size):
        population.sort()
        print(population[-1].genotype)
        hola = input()
        n = len(population) - pop_size
        selected_individuals = population[n:]
        return selected_individuals

class RouletteSelection(Selection):
    def select(self, population,pop_size):
        return GenericRouletteSelection.select(population,pop_size)

class GenericRouletteSelection(Selection):
    def select(population,pop_size):
        pairs = []
        selected = []
        length = 0
        total_fitness = 0
        
        for p in population:
            total_fitness += p.fitness 
            # print(p.fitness)

        accumulated = 0
        pairs.append((0,None))
        for p in population:
            accumulated += (p.fitness) / total_fitness
            pairs.append((accumulated,p))
        # for p in pairs:
        #     print("{} fitness {}".format(p[0],p[1]))
        

        while length < pop_size:

            for i in range(len(pairs)-1):
                
                r = random.uniform(0,1)
                
            
                if pairs[i][0] < r and r <= pairs[i+1][0]:
                    # print("R= {}".format(r))
                    # print("En i={}, pi = {}, pi+1 = {}".format(i,pairs[i][0],pairs[i+1][0]))
                    selected.append(pairs[i+1][1])
                    length += 1
                    
                    
        return selected

class RankSelection(Selection):
    def select(self, population,pop_size):

        new_pop = []
        population.sort(reverse=True)
        dict = {}
        selected = []
        
        for idx in range(len(population)):
            new_individual = copy.copy(population[idx])
            new_individual.fitness = (2*pop_size - idx -1) / (2*pop_size) 
            new_pop.append(new_individual)
            dict[hash(tuple(population[idx].genotype))] = population[idx]

        new_pop =  GenericRouletteSelection.select(new_pop,pop_size)
        for p in new_pop:
            selected.append(dict[hash(tuple(p.genotype))])

        return selected



class TournamentSelection(StochasticSelection):
    def select(self, population, pop_size):
        u = random.uniform(0.5,1)
        counter = 0
        others = []
        selected = []

        random.shuffle(population)

        while ( counter < pop_size):
            i = random.randint(counter+1,len(population)-1)
            others.append(population[i])
            del population[i]
            counter += 1


        for i in range(len(others)):
            
            r = random.uniform(0,1)
            if r < u:
                if population[i].fitness > others[i].fitness:
                    selected.append(population[i])
                else:
                    selected.append(others[i])
                
            else:
                if population[i].fitness > others[i].fitness:
                    selected.append(others[i])
                else:
                    selected.append(population[i])
                
        return selected

class BoltzmannSelection(StochasticSelection):
    def select(self, population, pop_size, iteration):
        T =  self.constant_temperature + (self.initial_temperature - self.constant_temperature) * exp(-self.k*iteration)
        dict = {}
        new_pop = []
        selected = []
        for p in population:
            new_individual = copy.copy(p)
            new_individual.fitness  = exp((p.fitness)/T)
            new_pop.append(new_individual)
            dict[hash(tuple(p.genotype))] = p


        new_pop =  GenericRouletteSelection.select(new_pop,pop_size)

        for p in new_pop:
            selected.append(dict[hash(tuple(p.genotype))])

        return selected

    def __init__(self, initial_temperature, constant_temperature, k, method_name):
        self.initial_temperature = initial_temperature
        self.constant_temperature = constant_temperature
        self.k = k
        self.method_name = method_name



class TruncatedSelection(StochasticSelection):
    
    def __init__(self, k, method_name):
        self.k = k
        self.method_name = method_name

    def select(self,population, pop_size):
        population.sort()
        population = population[self.k:]
        
        
        length = 0
        pop = []
        while (length<pop_size):
            i = random.randint(0,len(population)-1)
            pop.append(population[i])
            del population[i]
            length += 1
        
        return pop

def CreateSelection(selection):
    method = selection["selection_method"]
    initial_temperature = selection["initial_temperature"]
    constant_temp = selection["constant_temperature"]
    k = selection["k"]
    if method == "stochastic":
        sel = StochasticSelection(method)
    elif method == "elite":
        sel = EliteSelection(method)
    elif method == "roulette":
        sel = RouletteSelection(method)
    elif method == "rank":
        sel = RankSelection(method)
    elif method == "tournament":
        sel = TournamentSelection(method)
    elif method == "boltzmann":
        sel = BoltzmannSelection(initial_temperature, constant_temp, k, method)
    elif method == "truncated":
        sel = TruncatedSelection(k, method)
    else:
        return ("Error: invalid selection method.")
    return sel