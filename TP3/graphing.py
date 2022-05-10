from matplotlib import pyplot as plt
import numpy as np
from numpy import multiply

#function that reads i, error and w[] from resources/perceptron_data.txt and animates the different weights
def w_evolution():
    training_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    expected_output = [-1, -1, -1, 1]
    with open("resources/perceptron_data.txt", "r") as f:
        lines = f.readlines()
        i = []
        error = []
        w = []
        for line in lines:
            split = line.split("\t")
            i.append(int(split[0]))
            error.append(float(split[1]))
            split[2] = split[2].replace("\n", "").replace("[", "").replace("]", "")
            print("split[2] = " + split[2])
            aux = []
            for item in split[2].split("  "):
                aux.append(float(item))
            w.append(aux)
        f.close()

    # Plotting
    i = 0
    for weight in w:
        
        x1 = [-1, 1]
        m = -weight[1]/weight[2]
        c = weight[0]/weight[2]
        x2 = multiply(m,x1) + c
        for idx, item in enumerate(training_set):
            color =  "blue" if expected_output[idx] < 0 else "red"
            plt.scatter(item[0], item[1], color=color)
        plt.title("Iteration number: "+ str(i))
        s = "w = " + str(weight)+" error: "+ str(error[i])
        plt.plot(x1, x2, 'y-', label= s)
        plt.legend(loc='upper right')
        plt.pause(1)
        plt.clf()
        i += 1

def iterations_vs_learning_rate():
    #learning_rates.txt has following format: learning_rate \t iteration_ammount \t error (for it is an avarage of multiple runs)
    with open("resources/learning_rates.txt", "r") as f:
        lines = f.readlines()
        learning_rates = []
        iterations = []
        errors = []
        for line in lines:
            split = line.split(",")
            learning_rate = float(split[0])
            learning_rates.append(learning_rate)
            iteration = float(split[1])
            iterations.append(iteration)
            error = float(split[2])
            errors.append(error)
            #error bar is the standard deviation of the error
            #plt.plot(learning_rate, error, err = error, fmt="bo")
            plt.errorbar(learning_rate, error, yerr=error, fmt="bo")
        f.close()
        plt.show()


def error_vs_iteration(file_path, exp):
    #error_vs_iteration.txt has following format: iteration \t error 
    with open(file_path+ "/error_vs_iteration.txt", "r") as f:
        lines = f.readlines()
        iterations = []
        errors = []
        for line in lines:
            split = line.split(",")
            iteration = float(split[0])
            iterations.append(iteration)
            error = float(split[1])
            errors.append(error)
        f.close()
        plt.plot(iterations, errors)
        #if exp is true then set logarithmic scale for y axis
        if exp:
            plt.yscale('log')
        # set axis labels
        plt.xlabel("Epoch")
        plt.ylabel("Error")
        # set title
        # plt.title("Error vs iteration")
        plt.show()


#w_evolution()
# iterations_vs_learning_rate()