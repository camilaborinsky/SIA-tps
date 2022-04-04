import random 
#import config_parser as config

from classes.genotype import Individual


class GeneticCross:
    def cross(self, parent1: Individual, parent2: Individual):
        return parent1, parent2

    def __init__(self, method_name, reagents, exact_values):
        self.method_name = method_name
        self.reagents = reagents
        self.exact_values = exact_values
    

class UniformCross(GeneticCross):
    def cross(self, parent1: Individual, parent2: Individual):
        gen1 = []
        gen2 = []
        length = len(parent1.genotype)
        for x in range(0, length): #range is not inclusive with the second parameter, so range [0,len-1]
            random_number = random.random()
            if random_number < 0.5:
                gen1.append(parent1.genotype[x])
                gen2.append(parent2.genotype[x])
            else:
                gen1.append(parent2.genotype[x])
                gen2.append(parent1.genotype[x])

        child1 = Individual(gen1, self.exact_values, self.reagents)
        child2 = Individual(gen2, self.exact_values, self.reagents)

        return child1, child2




class MultipleCross(GeneticCross):

    def __init__(super, method_name,reagents, exact_values, multiple_method_n):
        super.multiple_method_n = multiple_method_n
        super.method_name = method_name
        super.reagents = reagents
        super.exact_values = exact_values


    def cross(self, parent1: Individual, parent2: Individual):
        gen1 = []
        gen2 = []
        length = len(parent1.genotype)
        
        random_indexes = random.sample(range(0,length-1), int(self.multiple_method_n))
        switched = False
        for x in range(0, length):
            if x in random_indexes:
                switched = not switched
            if switched:
                gen1.append(parent2.genotype[x])
                gen2.append(parent1.genotype[x])
            if not switched:
                gen1.append(parent1.genotype[x])
                gen2.append(parent2.genotype[x])
        
        child1 = Individual(gen1, self.exact_values, self.reagents)
        child2 = Individual(gen2, self.exact_values, self.reagents)

        return child1, child2

class SimpleCross(GeneticCross):
    def cross(self, parent1: Individual, parent2: Individual):
        gen1 = []
        gen2 = []
        length = len(parent1.genotype)
        random_index = random.randint(0, length-1)
        for x in range(0,length):
            if x < random_index:
                gen1.append(parent1.genotype[x])
                gen2.append(parent2.genotype[x])
            else:
                gen1.append(parent2.genotype[x])
                gen2.append(parent1.genotype[x])


        child1 = Individual(gen1, self.exact_values, self.reagents)
        child2 = Individual(gen2, self.exact_values, self.reagents)

        return child1, child2




def CreateCross(cross,reagents,exact_values):
    method = cross["cross_method"]
    multiple_method_n = cross["multiple_method_n"]
    
    if method == "uniform":
        c = UniformCross(method,reagents,exact_values)
    elif method == "multiple":
        c = MultipleCross(method,reagents,exact_values,multiple_method_n)
    elif method == "simple":
        c = SimpleCross(method,reagents,exact_values)
    else:
        return("Error: Cross method not valid.")
    return c
        

##Simple test. 
#parent1 = Individual([1,2,3,4,5,6,7,8,9,10,11], [4.4793, -4.0765, -4.0765,-4.1793, -4.9218, 1.7664,-3.9429, -0.7689, 4.883], [0, 1, 1])
#parent2 = Individual([12,13,14,15,16,17,18,19,20,21,22], [4.4793, -4.0765, -4.0765,-4.1793, -4.9218, 1.7664,-3.9429, -0.7689, 4.883], [0, 1, 1])
#cross = SimpleCross("simple")
#cross.cross(parent1, parent2)