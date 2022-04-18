

from abc import abstractmethod
from numpy import copy, dot, insert, multiply, random, zeros


class Perceptron:
    def __init__(self, expected_output, training_set, learn_rate):
        self.expected_output = expected_output
        self.training_set = training_set
        self.learn_rate = learn_rate
    
    def learn(self, iteration_limit):
        i = 0 #nro de iteracion
        p = len(self.training_set[0])
        w = zeros(p+1)
        # w = random.uniform(-1, 1, len(self.training_set[0]))
        error = 1
        self.error_min = 2*p
        while error > 0 and i < iteration_limit:
            idx = random.randint(0, len(self.training_set))
            cop = insert(copy(self.training_set[idx]), 0, -1)
            print("=================")
            print(cop)
            print(w)
            h = dot(cop, w, out=None)
            print(h)
            o = self.activation(h)
            w_diff = multiply(cop, self.learn_rate*(self.expected_output[idx]-o))
            w += w_diff
            error = self.calculate_error(self.training_set, self.expected_output, w, p)
            if error < self.error_min:
                self.error_min = error
                self.w_min = w
            i+=1
        print("W min"+ str(self.w_min))
        return self.w_min

    @abstractmethod
    def activation(self, h):
        pass

    @abstractmethod
    def calculate_error(self, real, expected, weights, p):
        pass

