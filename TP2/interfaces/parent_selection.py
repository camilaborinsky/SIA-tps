import random

class ParentSelection:
    def __init__(self, method_name):
        self.method_name = method_name
    
    def select(self, population):
        return population

class RandomSelection(ParentSelection):
    def select(self, population):
        targets = list(population)
        random.shuffle(targets)
        length = len(targets)
        return list(zip(targets[0:length//2], targets[length//2:]))



class SortedSelection(ParentSelection):
    def myfunction(individual):
        return individual.fitness

    def select (self, population):
        targets = list(population)
        targets.sort(key = self.myfunction)
        length = len(targets)
        return list(zip(targets[0:length//2], targets[length//2:]))



class BalancedSelection(ParentSelection):
    def select(self,population):
        targets = list(population)
        targets.sort()
        length = len(targets)
        list_of_pairs = []
        for i in range(length//2):
            list_of_pairs.append((targets[i],targets[length-1-i]))
        return list_of_pairs

def CreateParentSelection(method_name):
    if method_name == "random":
        return RandomSelection(method_name)
    elif method_name == "sorted":
        return SortedSelection(method_name)
    elif method_name == "balanced":
        return BalancedSelection(method_name)
    else:
        raise Exception("Unknown parent selection method: " + method_name)