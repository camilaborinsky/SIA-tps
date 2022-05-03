#multi layer perceptron class
import random

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
        for i in range(len(self.hidden_layers) + 1):
            if i == 0:
                self.weights[i] = np.random.uniform(-1, 1, size=(self.input_dim+1, self.hidden_layers[i] ) )
            elif i == len(self.hidden_layers):
                self.weights[i] = (np.random.uniform(-1, 1, size=(self.hidden_layers[i-1]+1, self.output_dim ) ) )
            else: 
                self.weights[i] = (np.random.uniform(-1, 1, size=(self.hidden_layers[i-1]+1, self.hidden_layers[i] ) ) )

        return self.weights

    #propagate input through network and get output
    def forward_propagation(self, input):
        if(len(input) != self.input_dim):
            print("Input dimension is not correct")
            return
        self.input = np.insert(input, 0, 1)
        self.hidden_outputs = {}
        self.output = []
        for i in range(len(self.hidden_layers) + 1):
            self.hidden_outputs[i] = np.matmul(self.input, self.weights[i])
            self.input = list(map(lambda h: self.activation(h), self.hidden_outputs[i]))
            self.input = np.insert(self.input, 0, 1)
        self.output = list(map(lambda h: self.activation(h), self.hidden_outputs[len(self.hidden_layers)]))
        return self.output
    
    #back propagate delta to adjust weights and return weights diff
    def back_propagation(self, expected):
        self.errors = {}
        weights_diff = {}
        for i in range(len(self.weights)-1, -1, -1):
            if i == len(self.weights)-1:
                self.errors[i] = np.multiply(np.subtract(expected, self.output), self.activation_derivative(self.hidden_outputs[i]))
            else:
                self.errors[i] = np.matmul( self.weights[i+1][1:, :], np.transpose(self.errors[i+1])) * self.activation_derivative(self.hidden_outputs[i])
            weights_diff[i] = np.dot(self.hidden_outputs[i], self.errors[i])

        return weights_diff
    

    #update weights with saved weights diff and return new weights
    def update_weights(self):
        for i in range(len(self.weights)-1, -1, -1):
            self.weights[i] -= self.learning_rate * self.weights_diff[i]
        return self.weights

    def train(self, training_set, expected_output, iteration_limit, callback):
        i = 0
        error = 1
        self.error_min = None
        self.weights = self.initialize_weights()
        while error > 0.0001 and i < iteration_limit:
            idx = random.randint(0, len(training_set)-1)
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
        return error/2