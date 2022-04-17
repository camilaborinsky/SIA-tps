from numpy import sign
from perceptrons.perceptron import Perceptron


class SimpleStepPerceptron(Perceptron):

    def activation(self, h):
       return h

    def error(real, expected, weights, p):
        error = 0
        for i in range(0,p):
            aux = 0
            for j in range(0,len(weights)):
                aux += weights[j]*real[i][j]
            error += (expected[i]-aux)**2
        error *= 0.5
        return error
            