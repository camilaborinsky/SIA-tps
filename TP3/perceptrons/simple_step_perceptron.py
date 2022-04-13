from numpy import sign
from perceptrons.perceptron import Perceptron


class SimpleStepPerceptron(Perceptron):

    def activation(self, h):
       return sign(h) 