import numpy as np


class Hopfield:

    def __init__(self, stored_inputs):
        self.stored_inputs = stored_inputs
        self.input_dim = len(stored_inputs[0])
    
    def initialize_weights(self):
        self.weights = np.zeros((self.input_dim, self.input_dim))
        for i in range(len(self.input_dim)):
            for j in range(i+1, len(self.input_dim)):
                w = self.calculate_weight(i, j)
                self.weights[i][j] = w
                self.weights[j][i] = w
    
    def calculate_weight(self, i, j):
        weight = 0
        if i == j:
            return weight
        for p in range(len(self.stored_inputs)):
            weight+=self.stored_inputs[p][i]*self.stored_inputs[p][j]
        return weight/len(self.stored_inputs)



    def train(self, input_value, iterations):
        self.initialize_weights()
        i=0
        current_state = input_value.copy()
        while i < iterations:
            h = np.matmul(current_state, self.weights)
            current_state = np.sign(h)
            i+=1
        
        for val in self.stored_inputs:
            if np.array_equal(val, current_state):
                return current_state, val
        return current_state, None