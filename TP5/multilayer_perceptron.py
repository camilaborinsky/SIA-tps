#multi layer perceptron class
from cmath import sqrt
from collections import Counter
import math
import random
import time
from matplotlib.pyplot import axis

import numpy as np

# from metrics import rmsd

alpha = 0.8

class MultiLayerPerceptron:
    def __init__(self, learning_rate, hidden_layers, input_dim, output_dim, update_frequency, 
    activation_function, activation_function_derivative, update_learn_rate, scale_output, momentum):
        self.learning_rate = learning_rate
        self.hidden_layers = hidden_layers
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.activation = activation_function
        self.activation_derivative = activation_function_derivative
        self.update_learn_rate = update_learn_rate
        self.scale_needed = scale_output
        self.error_k = 0
        self.update_frequency = update_frequency
        self.momentum = momentum
        self.old_delta_w = {}
        

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
                self.input = self.activation(self.hidden_outputs[i+1][1:])
                self.input = np.insert(self.input, 0, 1)
        self.output = self.activation(self.hidden_outputs[len(self.hidden_layers) +1])
        # self.output = list(map(lambda h: self.activation(h), self.hidden_outputs[len(self.hidden_layers)+1]))
        # if self.scale_needed ==True:
        #     return self.scale_output()
        return self.output

    def propagate(self, input_val,start, end):
        hidden_outputs = {}
        input_val = np.insert(input_val, 0, 1)
        hidden_outputs[0] = input_val
        output = []
        for i in range(start, end + 1):
            if(i == end):
                hidden_outputs[i+1] = np.matmul(input_val, self.weights[i])
            else:
                hidden_outputs[i+1] = np.insert(np.matmul(input_val, self.weights[i]), 0, 1)
                input_val = self.activation(self.hidden_outputs[i+1][1:])
                input_val = np.insert(input_val, 0, 1)
        output = self.activation(hidden_outputs[end+1])
        # self.output = list(map(lambda h: self.activation(h), self.hidden_outputs[len(self.hidden_layers)+1]))
        # if self.scale_needed ==True:
        #     return self.scale_output()
        return output
    
    #back propagate delta to adjust weights and return weights diff
    def back_propagation(self, expected):
        self.errors = {}
        weights_diff = {}
        if self.scale_needed == True:
            expected = self.normalize_output(expected)
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
            self.old_delta_w[i] = self.learning_rate * self.weights_diff[i]
        return self.weights

    def train(self, training_set, expected_output, epoch_limit, callback):
        i = 0
        e = 0
        epoch_set = set()
        error = 1
        self.error_min = None

        self.weights = self.initialize_weights()
        # self.min_output = min(expected_output)
        # self.max_output = max(expected_output)
        self.weights_diff = None  

        while error > 0.000001 and e < epoch_limit:
        #while e < 8:
            indexes = list(range(len(training_set)))
            np.random.shuffle(indexes)
            for idx in indexes:
                self.forward_propagation(training_set[idx])
                if self.update_frequency == 0:
                    self.weights_diff = self.back_propagation(expected_output[idx])
                    if self.momentum:
                        self.momentum_variation()
                    self.weights = self.update_weights()      
                else:
                    
                    dict1 = self.back_propagation(expected_output[idx])
                    dict2 = self.weights_diff
                    if self.weights_diff is None:
                        self.weights_diff = self.back_propagation(expected_output[idx])
                    else:
                        for key,values in dict1.items():
                            dict1[key] = values + dict2[key]
                        self.weights_diff = dict1
                    if self.momentum:
                        self.momentum_variation()    
                    #self.weights_diff = dict(Counter(self.back_propagation(expected_output[idx])) + Counter(self.weights_diff))
                    if e % self.update_frequency == 1 and len(epoch_set) == 0:
                        self.weights = self.update_weights()
                        self.weights_diff = None
                i+=1
            error = self.calculate_error(training_set, expected_output)
            if self.error_min is None or error < self.error_min:
                self.error_min = error
                self.weights_min = self.weights
            if callback is not None:
                callback(e, error, self.weights, self.output)

            e+=1
        return self.weights_min, self.error_min

    def calculate_error(self, training_set, expected_output):
        for i in range(len(expected_output)):
            output = self.forward_propagation(training_set[i])
            if self.scale_needed:
                expected = self.normalize_output(expected_output[i])
            else:
                expected = expected_output[i]
            error = 0
            for j in range(self.output_dim):
                error += (expected[j] - output[j])**2
            
        return error/len(training_set)

    def get_learning_rate(self, error, prev_error):
        if(self.update_learn_rate is None):
            return self.learning_rate

        if error > prev_error:    
            if self.error_k < 0:
                self.error_k = 0
            self.error_k+=1
        elif error < prev_error:
            if self.error_k > 0:
                self.error_k = 0
            self.error_k-=1   
             
        return self.update_learn_rate(self.learning_rate, self.error_k)
    
    def scale_output(self):
        new_output = list(map(lambda h: h *(self.max_output[0] - self.min_output[0])+ self.min_output[0], self.output) )
       
        return new_output
    
    def normalize_output(self, expected):
            new_output = list(map(lambda h: (h- self.min_output[0]) /(self.max_output[0] - self.min_output[0]), expected) )
            return new_output
           

    def momentum_variation(self):

        if len(self.old_delta_w) > 0:
            for i in range(len(self.weights)-1, -1, -1):
                self.weights_diff[i] += (alpha/self.learning_rate) * self.old_delta_w[i]
        

    # def test_network(self, test_set, expected_output):
    #     errors = []
    #     for i in range(len(test_set)):
    #         out = self.forward_propagation(test_set[i])
    #         if self.scale_needed:
    #             exp = self.normalize_output(expected_output[i])
    #         else:
    #             exp = expected_output[i]
    #         errors.append(np.abs(np.subtract(exp, out)))
    #     return rmsd(errors)
        