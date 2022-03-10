import json
import numpy as np

from classes.board import Board

def find_blank(board: Board):
    for idx, val in board.positions:
        if val == 0:
            return idx

def import_config():
    file = open('config.json')
    config = json.load(file)
    board_array = config["board"]
    board = Board(np.array(board_array).flatten()) #Me deja el board como un array 1D
    algorithm = config["algorithm"]
    heuristic = config["heuristic"]
    empty_space = find_blank(board)
    file.close()
    return board, algorithm, heuristic,empty_space