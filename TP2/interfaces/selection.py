import copy
import random
from math import exp



T = 1000
dT = 1

class Selection:
    def select(self, population, pop_size):
        return population

class StochasticSelection(Selection):
    def select(self, population, pop_size, prob):
        return population

class EliteSelection(Selection):
    def select(self, population, pop_size):
        population.sort()
        n = len(population) - pop_size
        selected_individuals = population[n:]
        return selected_individuals

class RouletteSelection(StochasticSelection):
    def select(self, population,pop_size):
        pairs = []
        selected = []
        length = 0
        total_fitness = 0
        
        for p in population:
            total_fitness += p.fitness 

        accumulated = 0
        pairs.append((0,None))
        for p in population:
            accumulated += (p.fitness) / total_fitness
            pairs.append((accumulated,p))

        while length < pop_size:

            for i in range(len(pairs)-1):
                
                r = random.uniform(0,1)
            
                if pairs[i][0] < r and r <= pairs[i+1][0]:
                    print("R= {}".format(r))
                    print("En i={}, pi = {}, pi+1 = {}".format(i,pairs[i][0],pairs[i+1][0]))
                    selected.append(pairs[i+1][1])
                    length += 1
                    
                    
        return selected

class RankSelection(StochasticSelection):
    def select(self, population,pop_size):

        new_pop = []
        population.sort(reverse=True)
        dict = {}
        selected = []

        for idx,p in population:
            new_individual = copy.copy(p)
            new_individual.fitness = (pop_size - idx -1) / pop_size  # Check -1
            new_pop.append(new_individual)
            dict[hash(tuple(p.genotype))] = p

        new_pop =  RouletteSelection(new_pop,pop_size)
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

        dict = {}
        new_pop = []
        selected = []
        for p in population:
            new_individual = copy.copy(p)
            new_individual.fitness  = exp((p.fitness)/(T- dT * iteration))
            new_pop.append(new_individual)
            dict[hash(tuple(p.genotype))] = p


        new_pop =  RouletteSelection(new_pop,pop_size)

        for p in new_pop:
            selected.append(dict[hash(tuple(p.genotype))])

        return selected

class TruncatedSelection(StochasticSelection):
    def select(population, pop_size, k):
        population.sort(reverse= True)
        population = population[k:]
        
        length = 0
        pop = []
        while (length<pop_size):
            i = random.randint(0,len(population)-1)
            pop.append(population[i])
            del population[i]
            length += 1
        
        return pop
