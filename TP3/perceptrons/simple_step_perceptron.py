from numpy import dot, sign
from perceptrons.perceptron import Perceptron


class SimpleStepPerceptron(Perceptron):

    def activation(self, h):
       return sign(h) 
    
    def calculate_error(self, real, expected, weights, p):
        sum = 0
        for i in range(len(real)):
            o = self.activation(dot(real[i], weights))
            sum += (o - expected[i])**2

        return sum/2