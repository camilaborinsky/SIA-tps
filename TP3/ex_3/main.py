from audioop import mul
from math import tanh
import numpy as np
from parso import parse
from metrics import ConfusionMatrix, accuracy, precision, recall, f1_score, tp_rate, fp_rate
#from graphing import error_vs_iteration
from perceptrons.multilayer_perceptron import MultiLayerPerceptron
#from utils.file_utils import write_error_vs_iteration

def parse_training(file_path):
    training_set = [] 
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
    return training_set



def parse_ej2(file_path):
    training_set = parse_training(file_path)
    expected_output = []

    with open(file_path+"/expected_ej2.txt") as f:
        for line in f:
            expected_output.append([int(item) for item in line.strip().split()])
    f.close()

    return training_set, expected_output


def parse_ej3(file_path):
        training_set = parse_training(file_path)
        expected_output = []

        with open(file_path+"/expected_ej3.txt") as f:
            number = []
            for line in f:
                number = []
                for item in line.split(","):
                    if(item != ""):
                        number.append(int(item))
                expected_output.append(number)
        f.close()


        return training_set, expected_output


def generate_input_with_noise(file_path, ammount_of_inputs):
    training_set = parse_training(file_path)

    #for every value in training_set change it to its opposite with probability 0.02 
    for i in range(len(training_set)):
        for j in range(len(training_set[i])):
            a=np.random.rand()
            if(a < 0.02):
                training_set[i][j] = (training_set[i][j] + 1) % 2

    #write the new training set to a file, in case it is needed
    with open(file_path+"/training_with_noise.txt", "w") as f:
        for number in training_set:
            for item in number:
                f.write(str(int(item)) + " ")
            f.write("\n")
    f.close()

    return training_set


def metrics_ej2(real, expected):
    matrix = ConfusionMatrix(real,expected,0) # Sets even as positive
    total_accuracy = accuracy(matrix)
    total_precision = precision(matrix)
    total_recall = recall(matrix)
    total_f1 = f1_score(matrix)
    total_tp_rate = tp_rate(matrix)
    total_fp_rate = fp_rate(matrix)
    return total_accuracy,total_precision,total_recall,total_f1,total_tp_rate,total_fp_rate


def metrics_ej3(real, expected):
    dim = 10
    total_accuracy = 0
    total_precision = 0
    total_recall = 0
    total_f1 = 0
    total_tp_rate = 0
    total_fp_rate = 0
    
    # Real should be in the form [1,2,3]
    matrix: ConfusionMatrix = None
    metrics = dict()
    for i in range(dim):
        
        matrix = ConfusionMatrix(real,expected,i)
        #print(str(matrix))
        metrics[i] = [accuracy(matrix), precision(matrix), recall(matrix), f1_score(matrix), tp_rate(matrix), fp_rate(matrix)]
        total_accuracy += accuracy(matrix)
        total_precision += precision(matrix)
        total_recall += recall(matrix)
        total_f1 += f1_score(matrix)
        total_tp_rate += tp_rate(matrix)
        total_fp_rate += fp_rate(matrix)
    #avg_accuracy,avg_precision,avg_recall,avg_f1,avg_tp_rate,avg_fp_rate /= 10
    return metrics
    # return total_accuracy/dim,total_precision/dim,total_recall/dim,total_f1/dim,total_tp_rate/dim,total_fp_rate/dim


def main():
    training_set, expected_output = parse_ej3("ex_3/resources/training")
    input_dimension = len(training_set[0])
    expected_output_dimension = len(expected_output[0])
    print("expected output dim: " + str(expected_output[0]))

    multilayer_perceptron = MultiLayerPerceptron(learning_rate=0.1, hidden_layers=[2], input_dim=input_dimension, output_dim=expected_output_dimension, update_frequency= 0, activation_function=np.vectorize(lambda x: np.tanh(x)), activation_function_derivative=np.vectorize(lambda x: 1-(np.tanh(x))**2), update_learn_rate=0.1, scale_output=False,momentum=False)
    multilayer_perceptron.train(training_set, expected_output, epoch_limit=100, callback=(lambda i, error, weights, output: print("Iteration: {}, Error: {}, Output: {}".format(i, error, str(output)))))
    output = multilayer_perceptron.scale_output()
    #error_vs_iteration("ex_3/resources/xor/training", False)
    noise_training_set = generate_input_with_noise("ex_3/resources/training", 10)
    prediction = multilayer_perceptron.forward_propagation(noise_training_set[1])
    
    print("the prediction is: " + str(prediction))

if __name__ == "__main__":
     main()


#generate_input_with_noise("ex_3/resources/training", 10)

#parse_training("ex_3/resources/training")

