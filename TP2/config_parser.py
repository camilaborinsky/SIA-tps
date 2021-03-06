import json
from interfaces.breaks import CreateBreak
from interfaces.cross import CreateCross

from interfaces.mutations import CreateMutation
from interfaces.parent_selection import CreateParentSelection
from interfaces.selection import CreateSelection

class Config: 
    def __init__(self, population_size, parent_selection_method, precision_degree, break_condition,execution_count, execution_variants, cross_method, mutation, selection, reagents, exact_values):
        self.population_size = population_size
        self.parent_selection_method = parent_selection_method
        self.precision_degree = precision_degree
        self.break_condition = break_condition
        self.execution_count = execution_count
        self.execution_variants = execution_variants
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
    parent_selection_method = CreateParentSelection(config["parent_selection_method"])
    precision_degree = config["precision_degree"]
    execution_count = config["execution_count"]
    execution_variants = config["execution_variants"]
    reagents = config["reagents"]
    exact_values = config["exact_values"]

    break_condition = CreateBreak(config["break"], precision_degree)

    crossbreeding = CreateCross(config["crossbreeding"],reagents,exact_values)

    mutation = CreateMutation(config["mutation"])

    selection = CreateSelection(config["selection"])
    
    

    return Config(population_size, parent_selection_method, precision_degree, break_condition, execution_count, execution_variants, crossbreeding, mutation, selection, reagents, exact_values)
    

def initialize_config(filepath):
    global config
    config = import_config(filepath)