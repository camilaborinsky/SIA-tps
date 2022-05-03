#multi layer perceptron class
import random
from matplotlib.pyplot import axis

import numpy as np


class MultiLayerPerceptron:
    def __init__(self, learning_rate, hidden_layers, input_dim, output_dim, activation_function, activation_function_derivative):
        self.learning_rate = learning_rate
        self.hidden_layers = hidden_layers
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.activation = activation_function
        self.activation_derivative = activation_function_derivative

    def initialize_weights(self):
        self.weights = {}
        self.layers = [self.input_dim] + self.hidden_layers + [self.output_dim]
        for i in range(len(self.layers)-1):
            self.weights[i] = np.random.uniform(-1, 1, size=(self.layers[i]+1, self.layers[i+1]))

        return self.weights

    #propagate input through network and get output
    def forward_propagation(self, input):
        if(len(input) != self.input_dim):
            print("Input dimension is not correct")
            return
        self.hidden_outputs = {}
        self.input = np.insert(input, 0, 1)
        self.hidden_outputs[0] = self.input
        self.output = []
        for i in range(len(self.hidden_layers) + 1):
            if(i == len(self.hidden_layers)):
                self.hidden_outputs[i+1] = np.matmul(self.input, self.weights[i])
            else:
                self.hidden_outputs[i+1] = np.insert(np.matmul(self.input, self.weights[i]), 0, 1)
                self.input = list(map(lambda h: self.activation(h), self.hidden_outputs[i+1][1:]))
                self.input = np.insert(self.input, 0, 1)
        self.output = list(map(lambda h: self.activation(h), self.hidden_outputs[len(self.hidden_layers)+1]))
        return self.output
    
    #back propagate delta to adjust weights and return weights diff
    def back_propagation(self, expected):
        self.errors = {}
        weights_diff = {}
        for i in range(len(self.weights)-1, -1, -1):
            if i == len(self.weights)-1:
                self.errors[i] = np.multiply(np.subtract(expected, self.output), self.activation_derivative(self.hidden_outputs[i+1]))
            else:
                self.errors[i] = np.matmul( self.weights[i+1], np.transpose(self.errors[i+1])) * self.activation_derivative(self.hidden_outputs[i+1])
                self.errors[i] = self.errors[i][1:]

            weights_diff[i] = np.matmul(np.transpose(np.matrix(self.hidden_outputs[i])), np.matrix(self.errors[i]))
            

        return weights_diff
    

    #update weights with saved weights diff and return new weights
    def update_weights(self):
        for i in range(len(self.weights)-1, -1, -1):
            self.weights[i] += self.learning_rate * self.weights_diff[i]
        return self.weights

    def train(self, training_set, expected_output, epoch_limit, callback):
        i = 0
        e = -1
        epoch_set = set()
        error = 1
        self.error_min = None


        self.weights = self.initialize_weights()
        while error > 0.0001 and e < epoch_limit:
            if len(epoch_set) == 0:
                e+=1
                epoch_set = set(range(len(training_set)))
            idx = random.choice(tuple(epoch_set))
            epoch_set.remove(idx)
            self.output = self.forward_propagation(training_set[idx])
            self.weights_diff = self.back_propagation(expected_output[idx])
            self.weights = self.update_weights()
            error = self.calculate_error(training_set, expected_output)
            if self.error_min is None or error < self.error_min:
                self.error_min = error
                self.weights_min = self.weights
            callback(i, error, self.weights, self.output)
            i+=1
        return self.weights_min

    def calculate_error(self, training_set, expected_output):
        error = 0
        for i in range(len(expected_output)):
            output = self.forward_propagation(training_set[i])
            for j in range(self.output_dim):
                error += (expected_output[i][j] - output[j])**2
        return error/len(training_set)