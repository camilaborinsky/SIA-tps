from classes.genotype import Individual
import random

##Temporarily hardcoded
mutation_constant= 0.05
mutation_a= 0.03

class GeneticMutation:
    def mutate(self, genotype : Individual):
        return genotype

class UniformMutation(GeneticMutation):
    def mutate(self, individual: Individual):
        for x in range(0, len(individual.genotype)):
            random_number = random.uniform(0,1)
            if random_number < mutation_constant:
                individual.genotype[x] = random.uniform(-mutation_a, mutation_a)
        return individual

class NormalMutation(GeneticMutation):
    def mutate(self, genotype : Individual):
        return super().mutate(genotype)