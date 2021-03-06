import json
import numpy as np
from classes.heuristics import Hamming, Inversions, Manhattan
from classes.point import Point
from constants import ConfigParams, Heuristic, SearchAlgorithm

from classes.board import Board

class Config:
    def __init__(self, algorithm, board: Board, empty_space: Point, heuristic):
        self.algorithm = algorithm
        self.board = board
        self.empty_space = empty_space
        self.heuristic = heuristic

def find_blank(board: Board):
    for idx, val in enumerate(board.positions):
        if val == 0:
            return Point(int(idx%3), int(idx/3))

def import_config(config_file_path: str)-> Config:
    try:
        file = open(config_file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f'No se encontro archivo de configuración. Por favor asegurarse de que "{config_file_path}" existe.')

    config = json.load(file)
        

    if config[ConfigParams.ALGORITHM.value] is None:  
        file.close()
        missing_argument_message(ConfigParams.ALGORITHM.value)
    if config[ConfigParams.BOARD.value] is None:
        file.close()
        missing_argument_message(ConfigParams.BOARD.value)

  
    board_array = config[ConfigParams.BOARD.value]
    board = Board(np.array(board_array).flatten().tolist()) #Me deja el board como un array 1D
    algorithm = config[ConfigParams.ALGORITHM.value]
    empty_space = find_blank(board)
    heuristic = None
    if algorithm == SearchAlgorithm.A_STAR.value or algorithm == SearchAlgorithm.LGS.value or algorithm == SearchAlgorithm.GGS.value:
        heuristic_name = config[ConfigParams.HEURISTIC.value]
        if heuristic_name == Heuristic.hamming.value:
            heuristic = Hamming()
        elif heuristic_name == Heuristic.manhattan.value:
            heuristic = Manhattan()
        elif heuristic_name == Heuristic.inversions.value:
            heuristic = Inversions()
        if heuristic is None:
            file.close()
            missing_argument_message(ConfigParams.HEURISTIC.value) 
   
    file.close()
    return Config(algorithm, board, empty_space, heuristic)


def missing_argument_message(parameter: str):
    raise ValueError(f'Error al parsear los parámetros. Falta: {parameter}')
