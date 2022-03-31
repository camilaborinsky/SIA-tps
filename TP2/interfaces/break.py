class AlgorithmBreak:
    def checkBreak(self, time, generation_metrics):
        return True


class GenerationCountBreak(AlgorithmBreak):
    def __init__(self, generation_count):
        self.generation_count = generation_count

    def checkBreak(self, time, current_generation):
        return current_generation.generation_number >= self.generation_count

class TimeBreak(AlgorithmBreak):
    def __init__(self, max_time):
        self.max_time = max_time

    def checkBreak(self, current_time, current_generation):
        return current_time >= self.max_time

class AcceptableSolutionBreak(AlgorithmBreak):
    def __init__(self, precision):
        self.precision = precision

    def checkBreak(self, time, current_generation):
        return current_generation.max_fitness <= self.precision

class ConstantSolutionBreak(AlgorithmBreak):
    def __init__(self, precision):
        self.precision = precision

    def checkBreak(self,  time, current_generation):
        return current_generation.max_fitness <= self.precision