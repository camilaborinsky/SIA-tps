class AlgorithmBreak:
    def checkBreak(self, time, generation_metrics):
        return True


class GenerationCountBreak(AlgorithmBreak):
    def __init__(self, generation_count, method_name):
        self.generation_count = generation_count
        self.method_name = method_name

    def checkBreak(self, time, current_generation_metrics):
        return current_generation_metrics.generation_number >= self.generation_count

class TimeBreak(AlgorithmBreak):
    def __init__(self, max_time, method_name):
        self.max_time = max_time
        self.method_name = method_name

    def checkBreak(self, time, current_generation_metrics):
        return time >= self.max_time

class AcceptableSolutionBreak(AlgorithmBreak):
    def __init__(self, precision, method_name):
        self.precision = precision
        self.method_name = method_name

    def checkBreak(self, time, current_generation_metrics):
        return abs(current_generation_metrics.max_fitness - 3) <= self.precision

class ConstantSolutionBreak(AlgorithmBreak):
    def __init__(self, precision, fixed_fitness, method_name):
        self.precision = precision
        self.fixed_fitness = fixed_fitness
        self.method_name = method_name

    def checkBreak(self, time, current_generation_metrics):
        return current_generation_metrics.max_fitness <= self.precision

def CreateBreak(break_cond, precision_degree):
    method = break_cond["end_criteria"]
    generation_limit = break_cond["generation_limit"]
    time_limit = break_cond["time_limit"]
    fixed_fitness = break_cond["fixed_fitness"]

    if method == "generation_count":
        b = GenerationCountBreak(generation_limit, method)
    elif method == "time":
        b = TimeBreak(time_limit, method)
    elif method == "acceptable_solution":
        b = AcceptableSolutionBreak(precision_degree, method)
    elif method == "constant_solution":
        b = ConstantSolutionBreak(precision_degree, fixed_fitness, method)
    else:
        return ("Error: Invalid break method.")
    return b

