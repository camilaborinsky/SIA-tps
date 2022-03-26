import random 

from classes.genotype import Individual


class GeneticCross:
    def cross(self, parent1: Individual, parent2: Individual):
        return parent1, parent2

class UniformCross(GeneticCross):
    def cross(self, parent1: Individual, parent2: Individual):
        return super().cross(parent1, parent2)

class MultipleCross(GeneticCross):
    def cross(self, parent1: Individual, parent2: Individual):
        return super().cross(parent1, parent2)

class SimpleCross(GeneticCross):
    def cross(self, parent1: Individual, parent2: Individual):
        child1 = parent1
        child2 = parent2
        random_index = random.randrange(0,10,1) #11 variable items in genotype: W, omega and omega_zero
        aux = parent1.genotype
        for i in range(random_index, 11):
            child1.genotype[i] = parent2.genotype[i]
            child2.genotype[i] = aux[i]
        return child1, child2
        