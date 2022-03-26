from functions import error

# W = [W0 ; W1; W2]
# w = [[w11 w12 w13], [w21 w22 w23]]
# w0 = [w01 w02]

class Individual:
    def __init__(self, genotype,exact_values, sigma):
        self.genotype = genotype
        self.fitness = self.calculate_fitness(exact_values, sigma)
    
    def get_genotype_elements(self):
        W = self.genotype[0:3]
        omega = self.genotype[3:9]
        omega_zero = self.genotype[9:11]
        return W, omega, omega_zero

    def calculate_fitness(self, exact_values, sigma):
        W, omega, omega_zero = self.get_genotype_elements()
        return (-1)* error(W, omega, omega_zero, exact_values,  sigma)


    def __eq__(self, other):
        if isinstance(other, Individual):
            return self.genotype == other.genotype
        return False

    def __hash__(self) -> int:
        return hash(self.genotype)

    def __lt__(self, other):
        return self.fitness > other.fitness
    
    def __le__(self, other):
        return self.fitness >= other.fitness