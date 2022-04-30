from perceptrons.multilayer_perceptron import MultiLayerPerceptron


def main():
    ml_perceptron = MultiLayerPerceptron(0.1, [2, 2], 2, 1, (lambda x: x), (lambda x: 1))
    print(str(ml_perceptron.initialize_weights()))
    ml_perceptron.forward_propagation([1, 1])
    ml_perceptron.calculate_error(1)


main()