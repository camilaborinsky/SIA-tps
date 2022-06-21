from math import ceil
import numpy as np
from scipy.optimize import minimize

class OptimizedAutoencoder:
    def __init__(self, optimizer, input_dim, latent_dim, hidden_layers, activation, activation_derivative):
        self.optimizer = optimizer
        self.input_dim = input_dim
        self.latent_dim = latent_dim
        self.hidden_layers = hidden_layers
        self.activation = activation
        self.activation_derivative = activation_derivative


    def initialize_weights(self):
        self.weights = list()
        reversed_hidden = self.hidden_layers.copy()
        reversed_hidden.reverse()
        self.layers = [self.input_dim] + self.hidden_layers + [self.latent_dim] + reversed_hidden + [self.input_dim]
        for i in range(len(self.layers)-1):
            # self.weights.append(np.random.uniform(-1, 1, size=(self.layers[i]+1, self.layers[i+1])))
            self.weights.append(np.random.uniform(-1, 1, size=(self.layers[i], self.layers[i+1])))

        return self.weights

    def flatten_weights(self):
        flat_weights = []
        for i in range(len(self.weights)):
            flat_weights.append(np.hstack(self.weights[i]))
        return np.hstack(flat_weights)

    def unpack_weights(self, flattened_weights):
        network = list()
        base_index = 0
        for i in range(len(self.weights)):
            curr_shape = self.weights[i].shape
            curr_length = curr_shape[0]*curr_shape[1]
            curr_weights = flattened_weights[base_index : base_index + curr_length].reshape(curr_shape)
            network.append(curr_weights)
            base_index+=curr_length
        # print("actualizamos weights")
        self.weights = network
        return network

    def forward_propagation(self, _input):
        # if(len(_input) != self.input_dim):
        #     print("Input dimension is not correct")
        #     return
        hidden_outputs = {}
        # _input = np.insert(_input, 0, 1)
        hidden_outputs[0] = _input
        output = []
        for i in range(len(self.layers)-1):
            if(i == len(self.layers)-2):
                hidden_outputs[i+1] = np.matmul(_input, self.weights[i])
            else:
                # hidden_outputs[i+1] = np.insert(np.matmul(_input, self.weights[i]), 0, 1)
                hidden_outputs[i+1] = np.matmul(_input, self.weights[i])

                _input = self.activation(hidden_outputs[i+1])
                # _input = np.insert(_input, 0, 1)
        output = self.activation(hidden_outputs[len(self.layers)-1 ])
        # self.output = list(map(lambda h: self.activation(h), self.hidden_outputs[len(self.hidden_layers)+1]))
        # if self.scale_needed ==True:
        #     return self.scale_output()
        return output

    def minimizer_callback(self, xk):
        error = self.calculate_error(self._input, self.output)
        self.errors.append(error)

    def train(self, _input, output, max_iterations):
        self.i = 0
        self.errors = list()
        self.initialize_weights()
        self._input = np.array(_input)
        self.output = np.array(output)
        
        flattened_weights = self.flatten_weights()
        res = minimize(fun=self.calculate_flattened_error, x0=flattened_weights,
        args=(0), method=self.optimizer, options={

            'maxiter': max_iterations,
            'adaptive': True,
            'disp': True,
        }, callback=self.minimizer_callback)

        self.unpack_weights(flattened_weights)

        error = res.fun
        return error, self.errors

    def calculate_error(self, training_set, expected_output):
        error = 0
        output = self.forward_propagation(training_set)
        
        expected = expected_output
        error += np.linalg.norm(np.subtract(output, expected))**2

            
        return error/len(training_set)


    def reconstruct(self, input_val):
        output= self.propagate(input_val, 0, len(self.layers)-2)
        error = np.linalg.norm(np.subtract(input_val, output), 2)
        return output, error 
        
    def calculate_flattened_error(self, flattened_weights, step=None):
        self.unpack_weights(flattened_weights)
        error = self.calculate_error(self._input, self.output)
        # if(self.i % 100 == 0):
        #     self.errors.append(error)
        self.i += 1
        return error

    def propagate(self, input_val,start, end):
        hidden_outputs = {}
        hidden_outputs[0] = input_val
        output = []
        for i in range(start, end + 1):
            if(i == end):
                hidden_outputs[i+1] = np.matmul(input_val, self.weights[i])
            else:
                hidden_outputs[i+1] = np.matmul(input_val, self.weights[i])
                input_val = self.activation(hidden_outputs[i+1])
        output = self.activation(hidden_outputs[end+1])
        return output


    def encode(self, input_val):
        return self.propagate(input_val, 0, int((len(self.layers)-2)/2))

    def decode(self, input_val):
        return self.propagate(input_val, int(ceil((len(self.layers)-2)/2)), int(len(self.layers)-2))

    def test_autoencoder(self, testing_set):
        avg_err = 0
        for val1, val2 in testing_set:
            out, err = self.reconstruct(val2)
            avg_err += err
        return avg_err/len(testing_set)

    def get_latent_space(self, testing_set):
        x_values = []
        y_values = []
        labels = []
        for i in testing_set:
            labels.append(i[0])
            aux = self.encode(i[1])
            x_values.append(aux[0])
            y_values.append(aux[1])
        return labels, x_values, y_values