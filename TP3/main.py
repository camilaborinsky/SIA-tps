from perceptrons.simple_step_perceptron import SimpleStepPerceptron


def main():
    training_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    expected_output = [-1, -1, -1, 1]
    p = SimpleStepPerceptron(expected_output, training_set, 0.1)
    p.learn(10)


main()
