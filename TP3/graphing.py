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


w_evolution()