#multi layer perceptron class
import random

import numpy as np


class MultiLayerPerceptron:
    def __init__(self, learning_rate, hidden_layers, input_dim, output_dim, activation_function, activation_function_derivative):
        self.learning_rate = learning_rate
        self.hidden_layers = hidden_layers
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.activation = activation_function,
        self.activation_derivative = activation_function_derivative

    def initialize_weights(self):
        self.weights = {}
        self.weights[0] = np.random.uniform(-1, 1, self.input_dim+1)
        for i in range(len(self.hidden_layers)):
            self.weights[i+1] = (np.random.uniform(-1, 1, self.hidden_layers[i]+1))
        self.weights[len(self.hidden_layers) + 1] = (np.random.uniform(-1, 1, self.output_dim))
        return self.weights

    #propagate input through network and get output
    def forward_propagation(self, input):
        print(type(self.activation))
        if(len(input) != self.input_dim):
            print("Input dimension is not correct")
            return
        self.input = np.insert(input, 0, 1)
        self.hidden_outputs = {}
        self.output = []
        for i in range(len(self.hidden_layers)):
            self.hidden_outputs[i] = (np.dot(self.input, self.weights[i]))
            self.input = self.activation(self.hidden_outputs[i])
            self.input = np.insert(self.input, 0, 1)
        self.hidden_outputs[-1] = np.dot(self.input, self.weights[-1])
        self.output = self.activation(self.hidden_outputs[-1])
        return self.output
    
    #back propagate delta to adjust weights and return weights diff
    def back_propagation(self, expected):
        self.errors = {}
        self.errors[-1] = (self.output - expected)*self.activation_derivative(self.hidden_outputs[-1])
        for i in range(len(self.hidden_layers), 0, -1):
            self.errors[i] = np.dot(self.errors[i+1], self.weights[i+1][1:]) * self.activation_derivative(self.hidden_outputs[i])
        weights_diff = {}
        for i in range(len(self.hidden_layers), 0, -1):
            weights_diff[i] = np.dot(self.input.T, self.errors[i])
        weights_diff[0] = np.dot(self.input.T, self.errors[0])
        
        return weights_diff
    

    #update weights with saved weights diff and return new weights
    def update_weights(self):
        for i in range(len(self.hidden_layers), 0, -1):
            self.weights[i] -= self.learning_rate * self.weights_diff[i]
        self.weights[0] -= self.learning_rate * self.weights_diff[0]
        return self.weights

    def train(self, training_set, expected_output, iteration_limit, callback):
        i = 0
        self.weights = self.initialize_weights()
        error = 1
        while error > 0 and i < iteration_limit:
            idx = random.randint(0, len(training_set))
            self.output = self.forward_propagation(training_set[idx])
            self.weights_diff = self.back_propagation(expected_output[idx])
            self.weights = self.update_weights()
            error = self.calculate_error(training_set, expected_output, self.weights, len(training_set))
            if error < self.error_min:
                self.error_min = error
                self.weights_min = self.weights
            callback(i, error, self.weights, self.output)
            i+=1
        return self.weights_min

    def calculate_error(self, expected_output):
        error = 0
        for i in range(len(expected_output)):
            error += (expected_output[i] - self.output[i])**2
        return error/len(expected_output)