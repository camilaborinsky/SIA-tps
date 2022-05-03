from graphing import error_vs_iteration
from perceptrons.simple_linear_perceptron import SimpleLinearPerceptron
from utils.file_utils import generate_linear_training, parse_training_set_from_file, write_error_vs_iteration


def main():
    generate_linear_training("resources/ex_2/testing", 5)
    training, expected = parse_training_set_from_file("resources/ex_2/testing")
    linear_perceptron  = SimpleLinearPerceptron(expected, training,  learn_rate=0.8)
    linear_perceptron.learn(iteration_limit=500, callback=(lambda i, error, weights : write_error_vs_iteration("resources/ex_2/testing", error[0], i)))
    error_vs_iteration("resources/ex_2/testing")
main()