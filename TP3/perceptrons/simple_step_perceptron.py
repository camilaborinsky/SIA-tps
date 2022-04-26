from numpy import copy, dot, insert, sign
from perceptrons.perceptron import Perceptron


class SimpleStepPerceptron(Perceptron):

    def activation(self, h):
       return sign(h) 