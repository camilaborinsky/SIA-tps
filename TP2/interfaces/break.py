class AlgorithmBreak:
    def checkBreak(self, param):
        return True


class GenerationCountBreak(AlgorithmBreak):
    def __init__(self, generation_count):
        self.generation_count = generation_count

    def checkBreak(self, current_generation):
        return current_generation >= self.generation_count

class TimeBreak(AlgorithmBreak):
    def __init__(self, max_time):
        self.max_time = max_time

    def checkBreak(self, current_time):
        return current_time >= self.max_time

class AcceptableSolutionBreak(AlgorithmBreak):
    def __init__(self, precision):
        self.precision = precision

    def checkBreak(self, max_fitness):
        return max_fitness <= self.precision

class ConstantSolutionBreak(AlgorithmBreak):
    def __init__(self, precision):
        self.precision = precision

    def checkBreak(self, max_fitness):
        return max_fitness <= self.precision