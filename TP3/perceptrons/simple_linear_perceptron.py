from numpy import copy, dot, insert
from perceptrons.perceptron import Perceptron


class SimpleLinearPerceptron(Perceptron):

    def activation(self, h):
       return h

    def calculate_error(self, real, expected, weights, p):
        sum = 0
        for i in range(len(real)):
            cop = insert(copy(real[i]), 0, -1)
            o = self.activation(dot(cop, weights))
            sum += (o - expected[i])**2

        return sum/2
            