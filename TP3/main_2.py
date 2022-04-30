from perceptrons.non_linear_perceptron import NonLinearPerceptron
from perceptrons.simple_linear_perceptron import SimpleLinearPerceptron
from utils.file_utils import parse_training_set_from_file, write_error_vs_iteration
from graphing import error_vs_iteration



def main():
    training, expected = parse_training_set_from_file("resources/ex_2/training")
    linear_perceptron  = SimpleLinearPerceptron(expected, training,  learn_rate=0.1)
    try:
        linear_perceptron.learn(iteration_limit=1000, callback=(lambda i, error, weights : write_error_vs_iteration("resources/ex_2/training", error, i) if i%10 == 0 else None))
    except Exception as e:
        print(e)
    error_vs_iteration("resources/ex_2/training", False)
main()