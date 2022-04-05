from classes.genotype import Individual
from numpy import random

##Temporarily hardcoded
mutation_constant= 0.05
mutation_a= 0.03


class GeneticMutation:
    def mutate(self, genotype : Individual):
        return genotype

    def __init__(self, probability, distribution_parameter, method_name):
        self.probability = probability
        self.distribution_parameter = distribution_parameter
        self.method_name = method_name


class UniformMutation(GeneticMutation):
    def mutate(self, individual: Individual):
        for x in range(0, len(individual.genotype)):
            random_number = random.rand(0,1)
            if random_number < mutation_constant:
                individual.genotype[x] += random.uniform(-mutation_a, mutation_a)
        return individual


class NormalMutation(GeneticMutation):
    def mutate(self, individual : Individual):
        for x in range(0, len(individual.genotype)):
            random_number = random.rand(0,1)
            if random_number < mutation_constant:
                individual.genotype[x] += random.normal(0, mutation_a)
        return individual



#for parsing input
def CreateMutation(mutation):
    method = mutation["method"]
    probability = mutation["probability"]
    distribution_param = mutation["distribution_parameter"]
    if method == "uniform":
        mut = UniformMutation(probability,distribution_param, method)
    elif method == "normal":
        mut = NormalMutation(probability, distribution_param, method)
    else: 
        return("Error: mutation name not valid")
    
    return mut


##Simple test
#parent1 = Individual([1,2,3,4,5,6,7,8,9,10,11], [4.4793, -4.0765, -4.0765,-4.1793, -4.9218, 1.7664,-3.9429, -0.7689, 4.883], [0, 1, 1])
#normalMutation = NormalMutation(0.1, 0.1, "normal")
#normalMutation.mutate(parent1)

