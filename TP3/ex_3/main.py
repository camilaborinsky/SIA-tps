from math import tanh
import numpy as np
from parso import parse
from graphing import error_vs_iteration
from perceptrons.multilayer_perceptron import MultiLayerPerceptron
from utils.file_utils import write_error_vs_iteration


def parse_training(file_path):
    training_set = []
    expected_output = []
    with open(file_path+"/training.txt") as f:
       #every 7 lines is a new training example, so we split the file into sets of 7 lines
        number = []
        i = 1
        for line in f: 
            for item in line.replace("\n", "").split(" "):
                if(item != ""):
                    number.append(float(item))
            if(i%7 == 0 and i != 0):
                training_set.append(number)
                number = []
            i += 1
    f.close()


    with open(file_path+"/expected.txt") as f:
        for line in f:
            expected_output.append([int(item) for item in line.strip().split()])
    f.close()

    return training_set, expected_output



def main():
    training_set, expected_output = parse_training("ex_3/resources/training")
    input_dimension = len(training_set[0])

    multilayer_perceptron = MultiLayerPerceptron(learning_rate=0.1, hidden_layers=[2], input_dim=input_dimension, output_dim=1, activation_function=np.vectorize(lambda x: np.tanh(x)), activation_function_derivative=np.vectorize(lambda x: 1 ))
    multilayer_perceptron.train(training_set, expected_output, iteration_limit=10000, callback=(lambda i, error, weights, output: print("Iteration: {}, Error: {}".format(i, error, weights))))
    #error_vs_iteration("ex_3/resources/xor/training", False)

if __name__ == "__main__":
     main()

#parse_training("ex_3/resources/training")




