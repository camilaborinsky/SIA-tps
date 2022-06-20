import numpy as np
from scipy.optimize import minimize

class OptimizedAutoencoder:
    def __init__(self, optimizer, input_dim, latent_dim, hidden_layers, activation):
        self.optimizer = optimizer
        self.input_dim = input_dim
        self.latent_dim = latent_dim
        self.hidden_layers = hidden_layers
        self.activation = activation


    def initialize_weights(self):
        self.weights = list()
        reversed_hidden = self.hidden_layers.copy()
        reversed_hidden.reverse()
        self.layers = [self.input_dim] + self.hidden_layers + [self.latent_dim] + reversed_hidden + [self.input_dim]
        for i in range(len(self.layers)-1):
            self.weights.append(np.random.uniform(-1, 1, size=(self.layers[i]+1, self.layers[i+1])))
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
        self.weights = network
        return network

    def forward_propagation(self, _input):
        if(len(_input) != self.input_dim):
            print("Input dimension is not correct")
            return
        hidden_outputs = {}
        _input = np.insert(_input, 0, 1)
        hidden_outputs[0] = _input
        output = []
        for i in range(len(self.layers)-1):
            if(i == len(self.layers)-2):
                hidden_outputs[i+1] = np.matmul(_input, self.weights[i])
            else:
                hidden_outputs[i+1] = np.insert(np.matmul(_input, self.weights[i]), 0, 1)
                _input = self.activation(hidden_outputs[i+1][1:])
                _input = np.insert(_input, 0, 1)
        output = self.activation(hidden_outputs[len(self.layers)-1 ])
        # self.output = list(map(lambda h: self.activation(h), self.hidden_outputs[len(self.hidden_layers)+1]))
        # if self.scale_needed ==True:
        #     return self.scale_output()
        return output


    def train(self, _input, output, max_iterations):
        self.errors = list()
        self.initialize_weights()
        
        flattened_weights = self.flatten_weights()

        res = minimize(fun=self.calculate_flattened_error, x0=flattened_weights, 
        args=(_input, output), method=self.optimizer, options={
            'maxfun': max_iterations,
            'maxfev': max_iterations,
            'maxiter': 1,
            'disp': True
        })

        self.unpack_weights(flattened_weights)

        error = res.fun
        return error, self.errors

    def calculate_error(self, training_set, expected_output):
        error = 0
        for i in range(len(expected_output)):
            output = self.forward_propagation(training_set[i])
            
            expected = expected_output[i]
            error += np.linalg.norm(np.subtract(output, expected), 2)**2
            # for j in range(self.input_dim):
            #     error += (expected[j] - output[j])**2
            
        return error/len(training_set)



        
    def calculate_flattened_error(self, flattened_weights, _input, expected_output):
        self.unpack_weights(flattened_weights)
        error = self.calculate_error(_input, expected_output)
        self.errors.append(error)
        return error
