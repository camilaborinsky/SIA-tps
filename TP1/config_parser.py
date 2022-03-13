import json
import numpy as np
from constants import ConfigParams, SearchAlgorithm

from classes.board import Board

class Config:
    def __init__(self, algorithm, board, empty_space, heuristic):
        self.algorithm = algorithm
        self.board = board,
        self.empty_space = empty_space,
        self.heuristic = heuristic

def find_blank(board: Board):
    for idx, val in enumerate(board.positions):
        if val == 0:
            return idx

def import_config(config_file_path: str)-> Config:
    try:
        file = open(config_file_path)
    except FileNotFoundError:
        raise ValueError(f'Configuration file not found. Please ensure "{config_file_path}" exists.')

    config = json.load(file)
        

    if config[ConfigParams.ALGORITHM.value] is None:  
        file.close()
        missing_argument_message(ConfigParams.ALGORITHM.value)
    if config[ConfigParams.BOARD.value] is None:
        file.close()
        missing_argument_message(ConfigParams.BOARD.value)

  
    board_array = config[ConfigParams.BOARD.value]
    board = Board(np.array(board_array).flatten()) #Me deja el board como un array 1D
    algorithm = config[ConfigParams.ALGORITHM.value]
    empty_space = find_blank(board)
    heuristic = None
    if algorithm == SearchAlgorithm.A_STAR or algorithm == SearchAlgorithm.LGS or algorithm == SearchAlgorithm.GGS:
        if config[ConfigParams.HEURISTIC.value] is None:
            missing_argument_message(ConfigParams.HEURISTIC.value)
        heuristic = config[ConfigParams.HEURISTIC.value]
   
    file.close()
    return Config(algorithm, board, empty_space, heuristic)


def missing_argument_message(parameter: str):
    raise ValueError(f'Error parsing arguments. Missing parameter: {parameter}')
