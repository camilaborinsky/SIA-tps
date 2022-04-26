from numpy import copy, dot, insert
from perceptrons.perceptron import Perceptron


class SimpleLinearPerceptron(Perceptron):

    def activation(self, h):
       return h
            