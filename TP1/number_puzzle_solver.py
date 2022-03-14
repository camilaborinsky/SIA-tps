import sys
from classes.heuristics import Heuristics
from constants import Heuristic, SearchAlgorithm
from classes import board, point, state, node
import config_parser
import time
import algorithms.bfs as bfs
import algorithms.dfs as dfs
import algorithms.a_star as a_star
import algorithms.vds as vds
# import algorithms.ggs as ggs
import algorithms.lgs as lgs
from output.visualization import render_tree




board = board.Board([1,2,3, 4, 6, 5, 7,8,0])
empty_space = point.Point(2,2)


    

def solve_puzzle(algorithm: SearchAlgorithm, initial_state:state.State, heuristic: Heuristics):
    #start timer
    if not initial_state.is_solvable():
        print("No solution")
        return
    initial_timestamp = time.time()
    print("Starting algorithm ", algorithm)
    # call solve method for corresponding algorithm

    if algorithm == SearchAlgorithm.BFS.value:
        output = bfs.solve(initial_state)
    elif algorithm == SearchAlgorithm.DFS.value:
        dfs.solve(initial_state)
    elif algorithm == SearchAlgorithm.A_STAR.value:
        a_star.solve(initial_state, heuristic)
    # elif algorithm == SearchAlgorithm.GGS.value:
    #     ggs.solve(initial_state, heuristic)
    elif algorithm == SearchAlgorithm.LGS.value:
        vds.solve(initial_state)
    elif algorithm == SearchAlgorithm.VDS.value:
        lgs.solve(initial_state, heuristic)
    

    #end timer
    final_timestamp = time.time()
    print("Processing time: ", final_timestamp - initial_timestamp)
    #print metrics
    return output


def main(config_file_path: str):
    config: config_parser.Config = config_parser.import_config(config_file_path)
    output = solve_puzzle(config.algorithm, state.State(config.board, config.empty_space), config.heuristic)
    if output.found_solution:
        print("nodos explotados: ", output.expanded_nodes)
        print("nodos frontera: ", output.frontier_nodes)
        # if len(output.solution) < 100:
        # render_tree(output.solution)







if __name__ == "__main__":
    argv = sys.argv

    config_file: str = 'config.json'
    if len(argv) > 1:
        config_file = argv[1]

    try:
        main(config_file)
    except FileNotFoundError:
        print("error")


 