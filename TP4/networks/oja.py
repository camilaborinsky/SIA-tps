import numpy as np
import random



class Oja:

    def __init__(self, stored_inputs, eta):
        self.stored_inputs = stored_inputs
        self.input_dim = len(stored_inputs)
        self.n = eta

    def initialize_weights(self):
        #np.random.rand((self.input_dim, self.input_dim))
        #self.weights = np.random.rand((self.input_dim, self.input_dim))
        w = []
        for i in range(len(self.stored_inputs[0])):
            w.append(random.uniform(-1.0,1.0))
        return np.array(w)
        
        
    
    def train(self, iterations):
        w = self.initialize_weights()
        for epoch in range(iterations):
            for i in range(self.input_dim):
                s = np.inner(self.stored_inputs[i], w)
                w = w + self.n * s * (self.stored_inputs[i] - s * w)
        return w
