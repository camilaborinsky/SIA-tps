

from abc import abstractmethod
from numpy import dot, random


class Perceptron:
    def __init__(self, expected_output, training_set, learn_rate):
        self.expected_output = expected_output
        self.training_set = training_set
        self.learn_rate = learn_rate
    
    def learn(self, iteration_limit):
        i = 0
        p = len(self.training_set)
        w = random.uniform(-1, 1, len(self.training_set[0])+1)
        error = 1
        error_min = 2*p
        while error > 0 and i < iteration_limit:
            idx = random.randint(0, p)
            h = dot(self.training_set[idx],w , out=None)
            o = self.activation(h)
            w_diff = self.learn_rate*(self.expected_output[idx]-o)*self.training_set[idx]
            w += w_diff
            error = self.calculate_error(self.training_set, self.expected_output, w, p)
            if error < error_min:
                error_min = error
                w_min = w
            i+=1
        return

    @abstractmethod
    def activation(h):
        pass

    @abstractmethod
    def calculate_error(real, expected, weights, p):
        pass

