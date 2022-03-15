

from matplotlib import pyplot as plt
from classes.board import Board
from classes.heuristics import Heuristics
from classes.state import State
from config_parser import Config, find_blank
from constants import Heuristic, SearchAlgorithm
from number_puzzle_solver import solve_puzzle

non_informed = [SearchAlgorithm.BFS, SearchAlgorithm.DFS]
boards = [
    Board([2, 5, 3, 1, 7, 4, 0, 8, 6]), 
    Board([1, 5, 8, 6, 0, 3, 4, 7, 2]), 
    Board([0, 1, 8, 4, 5, 7, 6, 3, 2]), 
    Board([6, 2, 5, 4, 1, 3, 8, 7, 0]),
    Board([7, 5, 1, 8, 4, 2, 0, 3, 6]),
    Board([2, 4, 5, 6, 3, 1, 7, 8, 0]),
    ]
informed = [SearchAlgorithm.LGS, SearchAlgorithm.A_STAR, SearchAlgorithm.GGS]
heuristics = [Heuristic.hamming, Heuristic.inversions, Heuristic.manhattan]

def generate_metrics():
    
    non_informed_outputs = dict()
    for board in boards:
        for alg in non_informed:
            config = Config(alg.value, board, find_blank(board), None)
            output = solve_puzzle(config.algorithm, State(config.board, config.empty_space), None)
            non_informed_outputs[(board, alg)] = output

    
    informed_outputs = dict()
    # for board in boards:
    #     for alg in informed:
    #         for heuristic in heuristics:
    #             config = Config(alg.value, board, find_blank(board), heuristic)
    #             output = solve_puzzle(config.algorithm.value, State(config.board, config.empty_space), heuristic)
    #             informed_outputs[(board, alg, heuristic)] = output
    

    return non_informed_outputs, informed_outputs



def save_graphs(non_informed_outputs, informed_outputs):
    for board, idx in boards:
        y = non_informed_outputs(non_informed).expanded_nodes
        fig, ax = plt.subplots()
        ax.bar(non_informed, y, width=1, edgecolor="white", linewidth=0.7)
        plt.savefig(f'output/graphs/board_{idx}_non_informed.png')

    


if __name__ == "__main__":
    save_graphs(generate_metrics())