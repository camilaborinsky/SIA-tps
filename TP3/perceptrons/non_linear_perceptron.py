from math import tanh,pow
from perceptrons.perceptron import Perceptron
from numpy import dot

beta = 1

class NonLinearPerceptron(Perceptron):

    def activation(self,h):
       return tanh(beta*h)     

    def activation_derivative(self,h):
        return beta*(1-pow(tanh(beta*h),2))