import numpy as np
from perceptrons.multilayer_perceptron import MultiLayerPerceptron
from perceptrons.non_linear_perceptron import NonLinearPerceptron
from perceptrons.simple_linear_perceptron import SimpleLinearPerceptron
from utils.file_utils import parse_training_set_from_file, write_error_vs_iteration
from graphing import error_vs_iteration



def main():
    training, expected = parse_training_set_from_file("ex_2/resources/training")
    multilayer_perceptron = MultiLayerPerceptron(learning_rate=0.2, hidden_layers=[], input_dim=len(training[0]), output_dim=len(expected[0]),update_frequency=0, activation_function=(lambda x: 1/(1+np.exp(-2*x))), activation_function_derivative=(lambda x: 2*(1/(1+np.exp(-2*x)))*(1-(1/(1+np.exp(-2*x)))) ), update_learn_rate=None, scale_output=True,momentum=False)
    weights, error = multilayer_perceptron.train(training, expected, epoch_limit=5, callback=(lambda i, error, weights, output: write_error_vs_iteration("ex_2/resources/training", error, i) if i%10 == 0 else None))
    # linear_perceptron  = SimpleLinearPerceptron(expected, training,  learn_rate=0.1)
    # try:
    #     linear_perceptron.learn(iteration_limit=1000, callback=(lambda i, error, weights : write_error_vs_iteration("resources/ex_2/training", error, i) if i%10 == 0 else None))
    # except Exception as e:
    #     print(e)
    print(weights)
    print(error)
    error_vs_iteration("ex_2/resources/training", False)
main()