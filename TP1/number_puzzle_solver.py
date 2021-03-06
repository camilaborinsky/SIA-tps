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
import algorithms.ggs as ggs
import algorithms.lgs as lgs
from output.visualization import render_config, render_stats, render_tree




    

def solve_puzzle(algorithm: SearchAlgorithm, initial_state:state.State, heuristic: Heuristics):
    #start timer
    if not initial_state.is_solvable():
        print("El estado inicial no tiene solución\n")
        return
    initial_timestamp = time.time()

    if algorithm == SearchAlgorithm.BFS.value:
        output = bfs.solve(initial_state)
    elif algorithm == SearchAlgorithm.DFS.value:
        output = dfs.solve(initial_state)
    elif algorithm == SearchAlgorithm.A_STAR.value:
        output = a_star.solve(initial_state, heuristic)
    elif algorithm == SearchAlgorithm.VDS.value:
        output = vds.solve(initial_state,10) #TODO: hacer que el json reciba el depth inicial y que no este harcodeado 
    elif algorithm == SearchAlgorithm.LGS.value:
        output = lgs.solve(initial_state, heuristic)
    elif algorithm == SearchAlgorithm.GGS.value:
        output = ggs.solve(initial_state, heuristic)
    

    #end timer
    final_timestamp = time.time()
    time_diff = final_timestamp - initial_timestamp
    print(f"Finalizada la ejecución de {algorithm}\n")    
    #print metrics
    return output, time_diff


def main(config_file_path: str):
    config: config_parser.Config = config_parser.import_config(config_file_path)
    render_config(config)
    output, time_diff = solve_puzzle(config.algorithm, state.State(config.board, config.empty_space), config.heuristic)
    if output is not None and output.found_solution:
        render_stats(output, time_diff)
        render_tree(output)
    else:
        print("No se encontró solución")







if __name__ == "__main__":
    argv = sys.argv

    config_file: str = 'config.json'
    if len(argv) > 1:
        config_file = argv[1]

    try:
        main(config_file)
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    


 