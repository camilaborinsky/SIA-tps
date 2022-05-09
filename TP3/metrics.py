
import random
from perceptrons.simple_step_perceptron import SimpleStepPerceptron
from perceptrons.simple_linear_perceptron import SimpleLinearPerceptron
from perceptrons.non_linear_perceptron import NonLinearPerceptron

BIAS : float = 0.1

class ConfusionMatrix:
    def __init__(self, real, expected, positive_value):
        tp = 0
        tn = 0
        fp = 0
        fn = 0

        for i in range(0,len(real)):
            if (abs(real[i] - expected[i]) < BIAS):
                if expected[i] == positive_value:
                    tp += 1
                else:
                    tn += 1
            else:
                if real[i] == positive_value:
                    fp += 1
                else:
                    fn += 1
                    
        self.tp = tp
        self.tn = tn
        self.fp = fp
        self.fn = fn
    def __str__(self):
     return "{}\t{}\n{}\t{}".format(self.tp,self.fn,self.fp,self.tn)   

def accuracy(confusion_matrix: ConfusionMatrix):
    try:
        return (confusion_matrix.tp + confusion_matrix.tn) / (confusion_matrix.tp + confusion_matrix.tn + confusion_matrix.fp + confusion_matrix.fn)
    except ZeroDivisionError:
        return 0

def precision(confusion_matrix: ConfusionMatrix):
    try:
        return confusion_matrix.tp / (confusion_matrix.tp + confusion_matrix.fp)
    except ZeroDivisionError:
        return 0

def recall(confusion_matrix: ConfusionMatrix):
    try:
        return confusion_matrix.tp / (confusion_matrix.tp + confusion_matrix.fn)
    except ZeroDivisionError:
        return 0

def f1_score(confusion_matrix: ConfusionMatrix):
    p = precision(confusion_matrix)
    r = recall(confusion_matrix)
    try:
        return (2*p*r) / (p+r)
    except ZeroDivisionError:
        return 0

def tp_rate(confusion_matrix: ConfusionMatrix):
    try:
        return recall(confusion_matrix)
    except ZeroDivisionError:
        return 0

def fp_rate(confusion_matrix: ConfusionMatrix):
    try:
        return confusion_matrix.fp / (confusion_matrix.fp + confusion_matrix.tn)
    except ZeroDivisionError:
        return 0

def cross_validation(p_class,training_set,k,iterations,expected,positive_value):
    # Shuffle and subdivide training set in k parts
    
    indexes = list(range(0,len(expected)))
    random.shuffle(indexes)
    shuffled_entry_set= []
    shuffled_expected = []
    
    q = len(indexes)//k    # Applies floor


    for j in range(0,k):
        aux_entry = []
        aux_expected = []
        for i in range(0,q):
            aux_entry.append(training_set[indexes[j*q+i]])
            aux_expected.append(expected[indexes[j*q+i]])
            #shuffled_entry_set[j].append(training_set[k*i:(k*(i+1))])
        shuffled_entry_set.append(aux_entry)
        shuffled_expected.append(aux_expected)
    print(shuffled_entry_set)
    print(shuffled_expected)

    # Training
    min_ws = []
    w = []
    for i in range(0,k-1):
        perceptron = p_class(expected,training_set,0.1)
        w = perceptron.learn(iterations, lambda i, error, weights: print("Iteration: {}, Error: {}, Weights:{}".format(i, error, weights)))
        min_ws.append(w)
        matrix = ConfusionMatrix(w,expected,positive_value)
        print("Matrix")
        print(str(matrix))
        acc = accuracy(matrix)
        print("Accuracy: {}".format(acc))
    print(min_ws)
    # Test
    #test(perceptron, shuffled_sets[k-1])


# Error Metrics

def mean_error(errors):
    total_error = 0
    for e in errors:
        total_error += e
    return total_error/len(errors)

def max_error(errors):
    return max(errors)

def min_error(errors):
    return min(errors)

# mean squared error
def mse(errors):
    total_error = 0
    for e in errors:
        total_error += pow(e,2)
    return total_error/len(errors)

# root mean square deviation
def rmsd(errors):
    return pow(mse(errors),0.5)
