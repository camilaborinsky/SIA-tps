
from matplotlib import pyplot as plt
import numpy as np
from classes.board import Board
from classes.heuristics import Hamming, Heuristics, Inversions, Manhattan
from classes.state import State
from config_parser import Config, find_blank
from constants import Heuristic, SearchAlgorithm
from number_puzzle_solver import solve_puzzle

non_informed = [SearchAlgorithm.BFS, SearchAlgorithm.DFS, SearchAlgorithm.VDS]
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

def generate_metrics(board_number):
    
    non_informed_outputs = dict()
    non_informed_times = dict()
    # for board in boards:
    for alg in non_informed:
        config = Config(alg.value, boards[board_number-1], find_blank(boards[board_number-1]), None)
        output, time_diff = solve_puzzle(config.algorithm, State(config.board, config.empty_space), None)
        non_informed_outputs[alg] = output
        non_informed_times[alg] = time_diff
    

    return non_informed_outputs, non_informed_times



def save_graphs(non_informed_outputs, non_informed_times, board_number):
        colors = ["#fa9a82", "#fcd874", "#827c7a", "#5996f7", "#c48cff"]

        labels = list(map(lambda alg: alg.value,non_informed))

        plt.xlabel('Algoritmo')
        plt.xticks(range(len(non_informed)), labels)
        plt.ylabel('Cantidad de nodos expandidos')
        y = list(map(lambda alg: non_informed_outputs[alg].expanded_nodes, non_informed))
        plt.bar(range(len(y)), y, width=1, edgecolor="white", linewidth=0.7, color= colors[0])
        plt.savefig(f'output/graphs/board_{board_number}_nf_expanded_nodes.png')
        plt.clf()
        plt.xlabel('Algoritmo')
        plt.xticks(range(len(non_informed)), labels)
        plt.ylabel('Cantidad de nodos frontera')
        y = list(map(lambda alg: len(non_informed_outputs[alg].frontier_nodes), non_informed))
        plt.bar(range(len(y)), y, width=1, edgecolor="white", linewidth=0.7, color= colors[1])
        plt.savefig(f'output/graphs/board_{board_number}_nf_frontier_nodes.png')
        plt.clf()
        plt.xlabel('Algoritmo')
        plt.xticks(range(len(non_informed)), labels)
        plt.ylabel('Cantidad de nodos explorados')
        y = list(map(lambda alg: len(non_informed_outputs[alg].explored_nodes), non_informed))
        plt.bar(range(len(y)), y, width=1, edgecolor="white", linewidth=0.7, color= colors[2])
        plt.savefig(f'output/graphs/board_{board_number}_nf_explored_nodes.png')
        plt.clf()
        plt.xlabel('Algoritmo')
        plt.xticks(range(len(non_informed)), labels)
        plt.ylabel('Tiempos de ejecuci??n')
        y = list(map(lambda alg: non_informed_times[alg], non_informed))
        plt.bar(range(len(y)), y, width=1, edgecolor="white", linewidth=0.7, color= colors[3])
        plt.savefig(f'output/graphs/board_{board_number}_nf_times.png')
        plt.clf()
        plt.xlabel('Algoritmo')
        plt.xticks(range(len(non_informed)), labels)
        plt.ylabel('Costo de soluci??n')
        y = list(map(lambda alg: non_informed_outputs[alg].final.depth, non_informed))
        plt.bar(range(len(y)), y, width=1, edgecolor="white", linewidth=0.7, color= colors[4])
        plt.savefig(f'output/graphs/board_{board_number}_nf_cost.png')


def generate_informed_metrics(board_number):
    informed_outputs = dict()
    informed_times = dict()
    # for board in boards:
    for alg in informed:
        config = Config(alg.value, boards[board_number-1], find_blank(boards[board_number-1]), None)
        output_hamming, time_diff_hamming = solve_puzzle(config.algorithm, State(config.board, config.empty_space), Hamming())
        output_manhattan, time_diff_manhattan = solve_puzzle(config.algorithm, State(config.board, config.empty_space), Manhattan())
        output_inversions, time_diff_inversions = solve_puzzle(config.algorithm, State(config.board, config.empty_space), Inversions())
        informed_outputs[alg] = [output_hamming, output_manhattan, output_inversions]
        informed_times[alg] = [time_diff_hamming, time_diff_manhattan, time_diff_inversions]
    
    return informed_outputs, informed_times

def save_informed_graphs(informed_outputs, informed_times, board_number):
        colors = ["#fa9a82", "#fcd874", "#827c7a", "#5996f7"]

        labels = list(map(lambda alg: alg.value,informed))
        ind = np.arange(len(informed)) 
        width = 0.2

        plt.xlabel('Algoritmo')
        plt.xticks(ind+width/3, labels)
        plt.ylabel('Cantidad de nodos expandidos')
        y0 = list(map(lambda alg: informed_outputs[alg][0].expanded_nodes, informed))
        y1 = list(map(lambda alg: informed_outputs[alg][1].expanded_nodes, informed))
        y2 = list(map(lambda alg: informed_outputs[alg][2].expanded_nodes, informed))
        plt.bar(ind, y0, width, edgecolor="white", linewidth=0.7, color= colors[0], label="hamming")
        plt.bar(ind+width, y1, width, edgecolor="white", linewidth=0.7, color= colors[1], label="manhattan")
        plt.bar(ind+2*width, y2, width, edgecolor="white", linewidth=0.7, color= colors[2], label="inversions")
        plt.legend(loc="best")
        plt.savefig(f'output/graphs/board_{board_number}_expanded_nodes.png')
        plt.clf()
        plt.xlabel('Algoritmo')
        plt.xticks(ind+width/3, labels)
        plt.ylabel('Cantidad de nodos explorados')
        y0 = list(map(lambda alg: len(informed_outputs[alg][0].explored_nodes), informed))
        y1 = list(map(lambda alg: len(informed_outputs[alg][1].explored_nodes), informed))
        y2 = list(map(lambda alg: len(informed_outputs[alg][2].explored_nodes), informed))
        plt.bar(ind, y0, width, edgecolor="white", linewidth=0.7, color= colors[0], label="hamming")
        plt.bar(ind+width, y1, width, edgecolor="white", linewidth=0.7, color= colors[1], label="manhattan")
        plt.bar(ind+2*width, y2, width, edgecolor="white", linewidth=0.7, color= colors[2], label="inversions")
        plt.legend(loc="best")
        plt.savefig(f'output/graphs/board_{board_number}_explored_nodes.png')
        plt.clf()
        
        plt.xlabel('Algoritmo')
        plt.xticks(ind+width/3, labels)
        plt.ylabel('Cantidad de nodos frontera')
        y0 = list(map(lambda alg: len(informed_outputs[alg][0].frontier_nodes), informed))
        y1 = list(map(lambda alg: len(informed_outputs[alg][1].frontier_nodes), informed))
        y2 = list(map(lambda alg: len(informed_outputs[alg][2].frontier_nodes), informed))
        plt.bar(ind, y0, width, edgecolor="white", linewidth=0.7, color= colors[0], label="hamming")
        plt.bar(ind+width, y1, width, edgecolor="white", linewidth=0.7, color= colors[1], label="manhattan")
        plt.bar(ind+2*width, y2, width, edgecolor="white", linewidth=0.7, color= colors[2], label="inversions")
        plt.legend(loc="best")
        plt.savefig(f'output/graphs/board_{board_number}_frontier_nodes.png')
        plt.clf()

        plt.xlabel('Algoritmo')
        plt.xticks(ind+width/3, labels)
        plt.ylabel('Tiempos de ejecuci??n')
        y0 = list(map(lambda alg: informed_times[alg][0], informed))
        y1 = list(map(lambda alg: informed_times[alg][1], informed))
        y2 = list(map(lambda alg: informed_times[alg][2], informed))
        plt.bar(ind, y0, width, edgecolor="white", linewidth=0.7, color= colors[0], label="hamming")
        plt.bar(ind+width, y1, width, edgecolor="white", linewidth=0.7, color= colors[1], label="manhattan")
        plt.bar(ind+2*width, y2, width, edgecolor="white", linewidth=0.7, color= colors[2], label="inversions")
        plt.legend(loc="best")
        plt.savefig(f'output/graphs/board_{board_number}_times.png')
        plt.clf()

        plt.xlabel('Algoritmo')
        plt.xticks(ind+width/3, labels)
        plt.ylabel('Costo de la soluci??n')
        y0 = list(map(lambda alg: informed_outputs[alg][0].final.depth, informed))
        y1 = list(map(lambda alg: informed_outputs[alg][1].final.depth, informed))
        y2 = list(map(lambda alg: informed_outputs[alg][2].final.depth, informed))
        plt.bar(ind, y0, width, edgecolor="white", linewidth=0.7, color= colors[0], label="hamming")
        plt.bar(ind+width, y1, width, edgecolor="white", linewidth=0.7, color= colors[1], label="manhattan")
        plt.bar(ind+2*width, y2, width, edgecolor="white", linewidth=0.7, color= colors[2], label="inversions")
        plt.legend(loc="best")
        plt.savefig(f'output/graphs/board_{board_number}_cost.png')
        plt.clf()
    



if __name__ == "__main__":
    # a, b = generate_metrics(5)
    # save_graphs(a, b, 5)
    c, d = generate_informed_metrics(5)
    save_informed_graphs(c, d, 5)