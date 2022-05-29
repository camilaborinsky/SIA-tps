

import random

import numpy as np


class KohonenNetwork:
    def __init__(self, input_dimension, output_dimension, initial_learning_rate):
        self.input_dimension = input_dimension
        self.output_dimension = output_dimension
        self.initial_radius = output_dimension/2
        self.initial_learning_rate = initial_learning_rate
        self.learning_rate = initial_learning_rate
        self.radius = self.initial_radius
    
    def initialize_grid(self, training_set):
        self.weights = [[None for l in range(self.output_dimension)] for k in range(self.output_dimension)]
        for row in range(self.output_dimension):
            for col in range(self.output_dimension):
                idx = np.random.randint(0, len(training_set))
                self.weights[row][col] = training_set[idx].copy()

    
    def get_activated_neuron(self, _input):
        min_distance = float('inf')
        to_return = []
        for i in range(self.output_dimension):
            for j in range(self.output_dimension):
                dist = self.calculate_distance(self.weights[i][j], _input)
                if dist < min_distance:
                    min_distance = dist
                    to_return=[(i,j, dist)]
                elif dist == min_distance:
                    to_return.append((i,j, dist))
        return random.choice(to_return)
    
    def calculate_distance(self, input1, input2):
        return np.linalg.norm(np.subtract(input1, input2), 2)
    
    def update_weights(self, i, j, _input):
        for row in range(self.output_dimension):
            for col in range(self.output_dimension):
                if self.calculate_distance([row, col], [i, j]) <= self.radius:
                    self.weights[row][col] += self.learning_rate * (_input - self.weights[row][col])
                    

    def train(self, training_set, input_ids, epochs, callback):
        self.p = len(training_set)
        self.initialize_grid(training_set)
        self.epochs = epochs
        self.data = list(zip(input_ids, training_set))
        self.radius_values = []
        self.learning_rate_values = []
        e = 0
        k=0
        while e < epochs:
            random.shuffle(self.data)
            for _input in self.data:
                self.radius_values.append(self.radius)
                self.learning_rate_values.append(self.learning_rate)
                i, j, d = self.get_activated_neuron(_input[1])
                self.update_weights(i, j, _input[1])               
                self.update_learn_rate(e, k)
                k+=1
            callback(e, self.get_quantization_error(training_set))
            e+=1
            self.update_radius(e, k)

    def update_learn_rate(self, e, k):
        self.learning_rate = self.initial_learning_rate*np.exp(-2*k/((self.epochs)*self.p))
        # self.learning_rate = self.initial_learning_rate * (1- (k) / ((self.epochs)*self.p))
    
    def update_radius(self, e, k):
        self.radius = self.initial_radius*np.exp(-5*k/((self.epochs)*self.p)) + 1
        # self.radius = self.initial_radius/2 * (2- (k+1) / ((self.epochs)*self.p))


    def u_matrix(self):
        u_matrix = np.zeros((self.output_dimension, self.output_dimension))
        for row in range(self.output_dimension):
            for col in range(self.output_dimension):
                available_dirs = 0
                if row > 0:
                    available_dirs +=1
                    u_matrix[row][col] += self.calculate_distance(self.weights[row][col], self.weights[row-1][col])
                if row < self.output_dimension-1:
                    available_dirs +=1
                    u_matrix[row][col] += self.calculate_distance(self.weights[row][col], self.weights[row+1][col])
                if col > 0:
                    available_dirs +=1
                    u_matrix[row][col] += self.calculate_distance(self.weights[row][col], self.weights[row][col-1])
                if col < self.output_dimension-1:
                    available_dirs +=1
                    u_matrix[row][col] += self.calculate_distance(self.weights[row][col], self.weights[row][col+1])
                u_matrix[row][col] /= available_dirs             
        return u_matrix
    
    def get_quantization_error(self, training_set):
        quantization_error = 0
        for _input in training_set:
            i, j, d = self.get_activated_neuron(_input)
            quantization_error += d
        return quantization_error/len(training_set)