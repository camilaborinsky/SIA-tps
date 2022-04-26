from matplotlib import pyplot as plt
from numpy import multiply
from perceptrons.simple_step_perceptron import SimpleStepPerceptron
from perceptrons.simple_linear_perceptron import SimpleLinearPerceptron
from perceptrons.non_linear_perceptron import NonLinearPerceptron

def main():
    training_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    expected_output = [-1, -1, -1, 1]
    p = SimpleStepPerceptron(expected_output, training_set, 0.1)
    #p = SimpleLinearPerceptron(expected_output, training_set, 0.1)
    #p = NonLinearPerceptron(expected_output, training_set, 0.1)
    w_min = p.learn(20)
    plot_decision_boundary(training_set, w_min, expected_output)

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


main()
