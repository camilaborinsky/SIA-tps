

import random

import numpy as np


class KohonenNetwork:
    def __init__(self, input_dimension, output_dimension, initial_learning_rate):
        self.input_dimension = input_dimension
        self.output_dimension = output_dimension
        self.initial_radius = output_dimension/2
        self.initial_learning_rate = initial_learning_rate
        self.learning_rate = initial_learning_rate,
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
                    to_return=[(i,j)]
                elif dist == min_distance:
                    to_return.append((i,j))
        # print(to_return)
        return random.choice(to_return)
    
    def calculate_distance(self, input1, input2):
        return np.linalg.norm(np.subtract(input1, input2), 2)
    
    def update_weights(self, i, j, _input):
        for row in range(self.output_dimension):
            for col in range(self.output_dimension):
                if self.calculate_distance([row, col], [i, j]) <= self.radius:
                    self.weights[row][col] += self.learning_rate * (_input - self.weights[row][col])
                    

    def train(self, training_set, input_ids, epochs):
        self.p = len(training_set)
        self.initialize_grid(training_set)
        self.epochs = epochs
        self.data = list(zip(input_ids, training_set))
        # print(self.data)
        e = 0
        k=0
        while e < epochs:
            random.shuffle(self.data)
            # print(e)
            # print(self.data)
            self.groups = [[list() for l in range(self.output_dimension)] for k in range(self.output_dimension)]
            for _input in self.data:
                i, j = self.get_activated_neuron(_input[1])
                # print(f"{i}, {j}")
                self.update_weights(i, j, _input[1])
               
                self.groups[i][j].append(_input[0])
                # print(self.groups)
                # print(self.radius)
                # print(self.learning_rate)

                self.update_learn_rate(e, k)
                k+=1
            e+=1
            self.update_radius(e, k)
        return e, self.groups

    def update_learn_rate(self, e, k):
        self.learning_rate = self.initial_learning_rate * (1- (k+1) / ((self.epochs)*self.p))
    
    def update_radius(self, e, k):
        self.radius = self.initial_radius * (1- (k+1) / ((self.epochs)*self.p))
