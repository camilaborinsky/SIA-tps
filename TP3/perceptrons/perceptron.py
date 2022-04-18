

from abc import abstractmethod
from numpy import dot, multiply, random


class Perceptron:
    def __init__(self, expected_output, training_set, learn_rate):
        self.expected_output = expected_output
        self.training_set = training_set
        self.learn_rate = learn_rate
    
    def learn(self, iteration_limit):
        i = 0 #nro de iteracion
        p = len(self.training_set)
        w = random.uniform(-1, 1, len(self.training_set[0]))
        error = 1
        self.error_min = 2*p
        while error > 0 and i < iteration_limit:
            idx = random.randint(0, p)
            h = dot(self.training_set[idx],w, out=None)
            o = self.activation(h)
            w_diff = multiply(self.training_set[idx], self.learn_rate*(self.expected_output[idx]-o))
            w += w_diff
            error = self.calculate_error(self.training_set, self.expected_output, w, p)
            if error < self.error_min:
                self.error_min = error
                self.w_min = w
            i+=1
            print(w)
        print("W min"+ str(self.w_min))
        return

    @abstractmethod
    def activation(self, h):
        pass

    @abstractmethod
    def calculate_error(self, real, expected, weights, p):
        pass

