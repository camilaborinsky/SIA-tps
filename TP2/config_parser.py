import json

from interfaces.mutations import CreateMutation

class Config: 
    def __init__(self, population_size, parent_selection_method, precision_degree, break_condition,execution_count, cross_method, mutation, selection, reagents, exact_values):
        self.parent_selection_method = parent_selection_method
        self.precision_degree = precision_degree
        self.break_condition = break_condition
        self.execution_count = execution_count
        self.population_size = population_size
        self.cross_method = cross_method
        self.mutation = mutation
        self.selection = selection
        self.reagents = reagents
        self.exact_values = exact_values

class BreakCondition:
    def __init__(self, break_condition):
        self.end_criteria = break_condition["end_criteria"]
        self.generation_limit = break_condition["generation_limit"]
        self.time_limit = break_condition["time_limit"]
        self.fixed_fitness = break_condition["fixed_fitness"]

class Cross:
    def __init__(self, cross):
        self.method = cross["cross_method"]
        self.multiple_method_n = cross["multiple_method_n"]

class Mutation:
    def __init__(self, mutation):
        self.method = mutation["method"]
        self.probability = mutation["probability"]
        self.distribution_parameter = mutation["distribution_parameter"]

class Selection:
    def __init__(self, selection):
        self.method = selection["selection_method"]
        self.parameter = selection["params"]

    
    
def import_config(config_file_path: str)-> Config:
    try:
        file = open(config_file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f'No se encontro archivo de configuración. Por favor asegurarse de que "{config_file_path}" existe.')
    
    config = json.load(file)
    population_size = config["population_size"]
    parent_selection_method = config["parent_selection_method"]
    precision_degree = config["precision_degree"]
    execution_count = config["execution_count"]

    break_condition = BreakCondition(config["break"])

    crossbreeding = Cross(config["crossbreeding"])

    mutation = CreateMutation(config["mutation"])
    print(mutation.probability, mutation.distribution_parameter)

    selection = Selection(config["selection"])
    
    reagents = config["reagents"]
    exact_values = config["exact_values"]

    return Config(population_size, parent_selection_method, precision_degree, break_condition, execution_count, crossbreeding, mutation, selection, reagents, exact_values)
    


config = import_config("config.json")