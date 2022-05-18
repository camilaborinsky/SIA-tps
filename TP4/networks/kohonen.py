

import random

import numpy as np


class KohonenNetwork:
    def __init__(self, input_dimension, output_dimension, initial_learning_rate):
        self.input_dimension = input_dimension
        self.output_dimension = output_dimension
        self.initial_radius = output_dimension/2
        self.initial_learning_rate = initial_learning_rate
    
    def initialize_grid(self, training_set):
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
                    to_return=[(i,j)]
                elif dist == min_distance:
                    to_return.append((i,j))
        return random.choice(to_return)
    
    def calculate_distance(self, input1, input2):
        return np.linalg.norm(np.subtract(input1 - input2), 2)
    
    def update_weights(self, i, j, _input):
        for row in range(self.output_dimension):
            for col in range(self.output_dimension):
                if self.calculate_distance([row, col], [i, j]) <= self.radius:
                    self.weights[row][col] += self.learning_rate * (_input - self.weights[row][col])
                    

    def train(self, training_set, epochs):
        p = len(training_set)
        self.initialize_grid(training_set)
        e = 0
        while e < epochs:
            random.shuffle(training_set)
            for _input in training_set:
                i, j = self.get_activated_neuron(_input)
                self.update_weights(i, j, _input)
            e+=1
