from matplotlib import pyplot as plt
from numpy import multiply
import numpy as np 
from perceptrons.simple_step_perceptron import SimpleStepPerceptron
from perceptrons.simple_linear_perceptron import SimpleLinearPerceptron
from perceptrons.non_linear_perceptron import NonLinearPerceptron

def main():
    training_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    expected_output = [[-1], [-1], [-1], [1]]
    p = SimpleStepPerceptron(expected_output, training_set, 0.1)
    #p = SimpleLinearPerceptron(expected_output, training_set, 0.1)
    #p = NonLinearPerceptron(expected_output, training_set, 0.1)
    #w_min = p.learn(20, lambda i, error, weights: print("Iteration: {}, Error: {}, Weights:{}".format(i, error, weights)))
    
    #w_min with lambda function that saves the values to a file
    #clear the file
    with open("resources/perceptron_data.txt", "w") as f:
        f.write("")
        f.close()
    w_min, i = p.learn(20, lambda i, error, weights: open("resources/perceptron_data.txt", "a").write("{}\t{}\t{}\n".format(i, error, weights)))
    plot_decision_boundary(training_set, w_min, expected_output)



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
    #TODO: a chequear esto, no estoy super segura que lo de desviacion estandar sea asi y con el avg... 
    error = np.std(iterations)
    #where iterations is centered
    avg_iterations = np.mean(iterations)
    open("resources/learning_rates.txt", "a").write("{},{},{}\n".format(learn_rate, avg_iterations, error))

    #plot_decision_boundary(training_set, w_min, expected_output)



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
        color =  "blue" if ex[idx] < 0 else "red"
        plt.scatter(item[0], item[1], color=color)
    plt.xlabel("feature 1")
    plt.ylabel("feature 2")
    plt.title("Perceptron Algorithm")
    plt.plot(x1, x2, 'y-')
    plt.show()


#main()
main_iteration_vs_learning_rate()