import json
from matplotlib import pyplot as plt
from numpy import multiply
import numpy as np 
from perceptrons.simple_step_perceptron import SimpleStepPerceptron
from perceptrons.simple_linear_perceptron import SimpleLinearPerceptron
from perceptrons.non_linear_perceptron import NonLinearPerceptron

""" def main():
    training_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    expected_output = [[1], [1], [-1], [-1]]
    p = SimpleStepPerceptron(expected_output, training_set, 0.1)
    #p = SimpleLinearPerceptron(expected_output, training_set, 0.1)
    #p = NonLinearPerceptron(expected_output, training_set, 0.1)
    #w_min = p.learn(20, lambda i, error, weights: print("Iteration: {}, Error: {}, Weights:{}".format(i, error, weights)))
    
    #w_min with lambda function that saves the values to a file
    #clear the file
    with open("resources/perceptron_data.txt", "w") as f:
        f.write("")
        f.close()
    w_min, error, i = p.learn(20, lambda i, error, weights: open("resources/perceptron_data.txt", "a").write("{}\t{}\t{}\n".format(i, error, weights)))
    plot_decision_boundary(training_set, w_min, expected_output) """

def main():
    config_file_path = "ex_1/resources/config.json"
    results_file_path = "ex_1/resources/perceptron_data.txt"
    learning_rates_results = "ex_1/resources/learning_rates.txt"
    open(results_file_path, "w").close()

    training_set, expected_output, learn_rate, epoch_limit, execution_count, random_weights = main.parse_config(config_file_path)
    p = SimpleStepPerceptron(expected_output, training_set, learn_rate)
    w_min, error_min, i = p.learn(epoch_limit*len(training_set), lambda i, error, weights: open(results_file_path, "a").write("{}\t{}\t{}\n".format(i, error, weights)), random_weights=random_weights)
    main.plot_decision_boundary(training_set, w_min, expected_output)
    


def main_iteration_vs_learning_rate():
    training_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    expected_output = [[-1], [-1], [-1], [1]]
    learn_rate = 0.9
    p = SimpleStepPerceptron(expected_output, training_set, learn_rate)

    iterations = []
    for count in range(5):
        w_min, i = p.learn(20, lambda i, error, weights: print("Iteration: {}, Error: {}, Weights:{}".format(i, error, weights)))
        print("W min"+ str(w_min) + " iteration: "+ str(i))

        iterations.append(i)
    error = np.std(iterations)
    #where iterations is centered
    avg_iterations = np.mean(iterations)
    open("resources/learning_rates.txt", "a").write("{},{},{}\n".format(learn_rate, avg_iterations, error))


def plot_decision_boundary(X, w, ex):
    
    # X --> Inputs
    # theta --> parameters
    
    # The Line is y=mx+c
    # So, Equate mx+c = theta0.X0 + theta1.X1 + theta2.X2
    # Solving we find m and c
    x1 = [-1, 1]
    m = -w[1]/w[2]
    c = w[0]/w[2]
    x2 = multiply(m,x1) + c
    
    # Plotting
    fig = plt.figure(figsize=(10,8))
    for idx, item in enumerate(X):
        color =  "blue" if ex[idx][0] < 0 else "red"
        plt.scatter(item[0], item[1], color=color)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Perceptron Algorithm")
    plt.plot(x1, x2, 'y-')
    plt.show()

def parse_config(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
        training_set = data["training_set"]
        expected_output = data["expected_output"]
        learn_rate = data["learn_rate"]
        epoch_limit = data["epoch_limit"]
        random_weights = bool(data["random_initial_weights"])
        execution_count = data["execution_count"]
        return training_set, expected_output, learn_rate, epoch_limit, execution_count, random_weights


def parse_results_for_rate(file_path):
    with open(file_path, "r") as f:
        iterations = []
        errors = []
        lines = f.readlines()
        for line in lines:
            i, e = line.strip().split(",")
            iterations.append(int(i))
            errors.append(float(e))
        return np.average(iterations), np.std(iterations), np.average(errors), np.std(errors)

def parse_rates_results(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        learn_rates = []
        iterations = []
        it_devs = []
        errors = []
        err_devs = []
        for line in lines:
            lr, i, i_dev, e, e_dev = line.strip().split(",")
            learn_rates.append(float(lr))
            iterations.append(float(i))
            it_devs.append(float(i_dev))
            errors.append(float(e))
            err_devs.append(float(e_dev))
        return learn_rates, iterations, it_devs, errors, err_devs

def iteration_vs_error(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        iterations = []
        errors = []
        for line in lines:
            i, e, w = line.strip().split("\t")
            iterations.append(int(i))
            errors.append(float(e))
        return iterations, errors

