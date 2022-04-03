import json
from interfaces.breaks import CreateBreak
from interfaces.cross import CreateCross

from interfaces.mutations import CreateMutation
from interfaces.selection import CreateSelection

class Config: 
    def __init__(self, population_size, parent_selection_method, precision_degree, break_condition,execution_count, cross_method, mutation, selection, reagents, exact_values):
        self.population_size = population_size
        self.parent_selection_method = parent_selection_method
        self.precision_degree = precision_degree
        self.break_condition = break_condition
        self.execution_count = execution_count
        self.cross_method = cross_method
        self.mutation = mutation
        self.selection = selection
        self.reagents = reagents
        self.exact_values = exact_values


    
    
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

    break_condition = CreateBreak(config["break"], precision_degree)

    crossbreeding = CreateCross(config["crossbreeding"])

    mutation = CreateMutation(config["mutation"])

    selection = CreateSelection(config["selection"])

    #print(break_condition.method_name, crossbreeding.method_name, mutation.method_name, selection.method_name)
    
    reagents = config["reagents"]
    exact_values = config["exact_values"]

    return Config(population_size, parent_selection_method, precision_degree, break_condition, execution_count, crossbreeding, mutation, selection, reagents, exact_values)
    

def init():
    global config
    config = import_config("config.json")