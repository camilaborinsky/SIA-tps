import numpy as np
import perceptrons.multilayer_perceptron as mlp
from perceptrons.non_linear_perceptron import NonLinearPerceptron
from perceptrons.simple_linear_perceptron import SimpleLinearPerceptron
from utils.file_utils import parse_training_set_from_file, write_error_vs_iteration
from graphing import error_vs_iteration
import utils.file_utils as fu



def main():
    # training, expected = parse_training_set_from_file("ex_2/resources/training")
    # multilayer_perceptron = MultiLayerPerceptron(learning_rate=0.2, hidden_layers=[], input_dim=len(training[0]), output_dim=len(expected[0]),update_frequency=0, activation_function=(lambda x: 1/(1+np.exp(-2*x))), activation_function_derivative=(lambda x: 2*(1/(1+np.exp(-2*x)))*(1-(1/(1+np.exp(-2*x)))) ), update_learn_rate=None, scale_output=True,momentum=False)
    # weights, error = multilayer_perceptron.train(training, expected, epoch_limit=5, callback=(lambda i, error, weights, output: write_error_vs_iteration("ex_2/resources/training", error, i) if i%10 == 0 else None))
    # # linear_perceptron  = SimpleLinearPerceptron(expected, training,  learn_rate=0.1)
    # # try:
    # #     linear_perceptron.learn(iteration_limit=1000, callback=(lambda i, error, weights : write_error_vs_iteration("resources/ex_2/training", error, i) if i%10 == 0 else None))
    # # except Exception as e:
    # #     print(e)
    # print(weights)
    # print(error)
    # error_vs_iteration("ex_2/resources/training", False)
    config_file_path = "ex_2/resources/config.json"
    config_file = fu.parse_config(config_file_path)

    path_to_data = config_file["path_to_data"]
    epoch_limit = int(config_file["epoch_limit"])
    execution_count = int(config_file["execution_count"])
    momentum = bool(config_file["momentum"])
    cross_validation_k = int(config_file["cross_validation"])
    learn_rate = float(config_file["learn_rate"])
    adaptive_learn_rate = bool(config_file["adaptive_learn_rate"])
    if adaptive_learn_rate:
        update_learn_rate = (lambda lr, k: lr + 0.3 if k >= 3 else (lr - lr*0.1 if k <=-3 else 0)) 
    else:
        update_learn_rate = None
    if config_file["activation_function"] == "linear":
        activation_function = (lambda x: x)
        activation_derivative = (lambda x: 1)
    elif config_file["activation_function"] == "sigmoid":
        activation_function = (lambda x: 1/(1+np.exp(-2*x)))
        activation_derivative = (lambda x: 2*(1/(1+np.exp(-2*x)))*(1-(1/(1+np.exp(-2*x)))) )

    training, expected = fu.parse_training_set_from_file(path_to_data)
    p = mlp.MultiLayerPerceptron(learning_rate=learn_rate, hidden_layers=[], input_dim=len(training[0]), output_dim=len(expected[0]), update_frequency=0, activation_function=activation_function, activation_function_derivative=activation_derivative, update_learn_rate=update_learn_rate, scale_output=True,momentum=momentum)
    p.train(training, expected, epoch_limit, callback=None)