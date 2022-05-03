from math import tanh
import numpy as np
from graphing import error_vs_iteration
from perceptrons.multilayer_perceptron import MultiLayerPerceptron
from utils.file_utils import write_error_vs_iteration


def main():
    training_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    expected_output = [[-1], [-1], [-1], [1]]

    multilayer_perceptron = MultiLayerPerceptron(learning_rate=0.1, hidden_layers=[2], input_dim=2, output_dim=1, activation_function=np.vectorize(lambda x: np.sign(x)), activation_function_derivative=np.vectorize(lambda x: 1 ))
    multilayer_perceptron.train(training_set, expected_output, iteration_limit=1000, callback=(lambda i, error, weights, output: write_error_vs_iteration("ex_3/resources/xor/training", error, i) if i%1 == 0 else None))
    error_vs_iteration("ex_3/resources/xor/training", False)
if __name__ == "__main__":
    main()
