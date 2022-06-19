from base64 import encode
from math import ceil
from matplotlib import pyplot as plt, scale
import numpy as np
from multilayer_perceptron import MultiLayerPerceptron


class Autoencoder:
    def __init__(self, 
    input_dim, 
    hidden_layers, 
    latent_dim, 
    activation_function, 
    activation_function_derivative, 
    update_learn_rate,
    learning_rate,
    update_frequency,
    momentum,
    use_adam):
        self.learning_rate = learning_rate
        decoder_layers = hidden_layers.copy()
        decoder_layers.reverse()
        self.hidden_layers = hidden_layers+[latent_dim] + decoder_layers
        print(len(self.hidden_layers))
        self.input_dim = input_dim
        self.output_dim = input_dim
        self.activation = activation_function
        self.activation_derivative = activation_function_derivative
        self.update_learn_rate = update_learn_rate
        self.update_frequency = update_frequency
        self.momentum = momentum
        self.use_adam = use_adam
        self.init_multilayer()

    
    def init_multilayer(self):
        self.multilayer_perceptron = MultiLayerPerceptron(self.learning_rate, self.hidden_layers, 
        self.input_dim, self.output_dim, update_frequency=self.update_frequency, activation_function=self.activation, 
        activation_function_derivative=self.activation_derivative, update_learn_rate=self.update_learn_rate, 
        scale_output=False, momentum=self.momentum, use_adam=self.use_adam)

    
    def train(self, training_set, expected_output, epoch_limit, callback):
        if(expected_output is None):
            expected_output=training_set
        return self.multilayer_perceptron.train(training_set, expected_output, epoch_limit, callback)

    def reconstruct(self, input_val):
        output= self.multilayer_perceptron.forward_propagation(input_val)
        error = np.linalg.norm(np.subtract(input_val, output), 2)
        return output, error 

    def encode(self, input_val):
        return self.multilayer_perceptron.propagate(input_val, 0, int(len(self.hidden_layers)/2))

    def decode(self, input_val):
        return self.multilayer_perceptron.propagate(input_val, int(ceil(len(self.hidden_layers)/2)), int(len(self.hidden_layers)))


    def graph_latent_space(self, training_set):
        plt.figure(figsize=(6,6))
        for i in training_set:
            aux = self.encode(i)

            plt.scatter(aux[0], aux[1], cmap='viridis')
        plt.show()
            
