from classes.genotype import Individual
import random

##Temporarily hardcoded
mutation_constant= 0.05
mutation_a= 0.03

class GeneticMutation:
    def mutate(self, genotype : Individual):
        return genotype

    def __init__(self, probability, distribution_parameter):
        self.probability = probability
        self.distribution_parameter = distribution_parameter


class UniformMutation(GeneticMutation):
    def mutate(self, individual: Individual):
        for x in range(0, len(individual.genotype)):
            random_number = random.rand(0,1)
            if random_number < mutation_constant:
                individual.genotype[x] += random.uniform(-mutation_a, mutation_a)
        return individual

class NormalMutation(GeneticMutation):
    def mutate(self, genotype : Individual):
        return super().mutate(genotype)



#for parsing input
def CreateMutation(mutation):
    method = mutation["method"]
    probability = mutation["probability"]
    distribution_param = mutation["distribution_parameter"]
    if method == "uniform":
        mut = UniformMutation(probability,distribution_param)
    elif method == "normal":
        mut = NormalMutation(probability, distribution_param)
    else: 
        return("Error: mutation name not valid")
    
    return mut


