class Individual:
    def __init__(self, genotype):
        self.genotype = genotype
    
    def get_genotype_elements(self):
        W = self.genotype[0:3]
        omega = self.genotype[3:9]
        omega_zero = self.genotype[9:11]
        
        return W, omega, omega_zero