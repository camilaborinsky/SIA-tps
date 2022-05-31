import numpy as np


class Hopfield:

    def __init__(self, stored_inputs):
        self.stored_inputs = np.array(stored_inputs)
        self.input_dim = len(stored_inputs[0])
    
    def initialize_weights(self):
        weights = np.dot(self.stored_inputs.T, self.stored_inputs)
        np.fill_diagonal(weights, 0)
        return weights/self.input_dim
        # self.weights = np.zeros((self.input_dim, self.input_dim))
        # for i in range(len(self.input_dim)):
        #     for j in range(i+1, len(self.input_dim)):
        #         w = self.calculate_weight(i, j)
        #         self.weights[i][j] = w
        #         self.weights[j][i] = w
    
    def calculate_weight(self, i, j):
        weight = 0
        if i == j:
            return weight
        for p in range(len(self.stored_inputs)):
            weight+=self.stored_inputs[p][i]*self.stored_inputs[p][j]
        return weight/len(self.stored_inputs)



    def train(self, input_value, iterations):
        self.weights = self.initialize_weights()
        i=0
        vector_of_states = []
        energy_values = []
        previous_state = np.zeros(self.input_dim)
        current_state = input_value.copy()
        while i < iterations and not np.array_equal(current_state, previous_state):
            previous_state = current_state.copy()
            energy_values.append(self.calculate_energy(current_state))
            h = np.matmul(current_state, self.weights)
            current_state = np.sign(h)
            for j,s in enumerate(current_state):
                current_state[j] = s if s != 0 else previous_state[j]
            vector_of_states.append(current_state)
            i+=1
        
        for val in self.stored_inputs:
            if np.array_equal(val, current_state):
                return current_state, val, i, vector_of_states, energy_values
        return current_state, None, i, vector_of_states, energy_values

    def calculate_energy(self, state):
        energy = 0
        for i in range(self.input_dim):
            for j in range(i, self.input_dim):
                energy += self.weights[i][j]*state[i]*state[j]
        return -energy