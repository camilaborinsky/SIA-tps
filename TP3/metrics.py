
import random
from perceptrons.simple_step_perceptron import SimpleStepPerceptron
from perceptrons.simple_linear_perceptron import SimpleLinearPerceptron
from perceptrons.non_linear_perceptron import NonLinearPerceptron

BIAS : float = 0.1

class ConfusionMatrix:
    def __init__(self, real, expected):
        tp = 0
        tn = 0
        fp = 0
        fn = 0

        for i in range(0,len(real)):
            if (abs(real[i] - expected[i]) < BIAS):
                if expected[i] == 1:
                    tp += 1
                else:
                    tn += 1
            else:
                if expected[i] == 1:
                    fn += 1
                else:
                    fp += 1
        self.tp = tp
        self.tn = tn
        self.fp = fp
        self.fn = fn
    def __str__(self):
     return "{}\t{}\n{}\t{}".format(self.tp,self.fn,self.fp,self.tn)   

def accuracy(confusion_matrix: ConfusionMatrix):
    return (confusion_matrix.tp + confusion_matrix.tn) / (confusion_matrix.tp + confusion_matrix.tn + confusion_matrix.fp + confusion_matrix.fn)

def precision(confusion_matrix: ConfusionMatrix):
    return confusion_matrix.tp / (confusion_matrix.tp + confusion_matrix.fp)

def recall(confusion_matrix: ConfusionMatrix):
    return confusion_matrix.tp / (confusion_matrix.tp + confusion_matrix.fn)

def f1_score(confusion_matrix: ConfusionMatrix):
    p = precision(confusion_matrix)
    r = recall(confusion_matrix)
    return (2*p*r) / (p+r)

def tp_rate(confusion_matrix: ConfusionMatrix):
    return recall(confusion_matrix)

def fp_rate(confusion_matrix: ConfusionMatrix):
    return confusion_matrix.fp / (confusion_matrix.fp + confusion_matrix.tn)

def cross_validation(p_class,training_set,k,iterations,expected):
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
        matrix = ConfusionMatrix(w,expected)
        print("Matrix")
        print(str(matrix))
        acc = accuracy(matrix)
        print("Accuracy: {}".format(acc))
    print(min_ws)
    # Test
    #test(perceptron, shuffled_sets[k-1])

# k= 3
# iterations = 20
# training_set = [0,1,2,3,4,5,6,7,8]
# cross_validation(perceptron,training_set,k,20)

# k = 3
# training_set = [5,2,3, 4, 1, 6]
# expected = [2,1, 4, 5, 6, 3]
# cross_validation(NonLinearPerceptron,training_set,k,20,expected)
