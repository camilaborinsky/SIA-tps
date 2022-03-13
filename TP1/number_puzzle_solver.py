import sys
from constants import SearchAlgorithm
from classes import board, point, state, node
import config_parser
import time


board = board.Board([1,2,3, 4, 6, 5, 7,8,0])
empty_space = point.Point(2,2)


    

def solve_puzzle(algorithm: SearchAlgorithm, initial_state:state.State):
    #start timer
    initial_timestamp = time.time()
    print("Starting algorithm ", algorithm)
    # call solve method for corresponding algorithm
    
    # p1 = point.Point(3,3)
    # print(p1.get_movements(3,3))
    # p1.move(movement.Movement.Right)
    # print(p1)
    incorrect_state = state.State(board, empty_space)
    print(incorrect_state.is_final())
    

    #end timer
    final_timestamp = time.time()
    print("Processing time: ", final_timestamp - initial_timestamp)
    #print metrics


def main(config_file_path: str):
    board, algorithm, heuristic,empty_space = config_parser.import_config()
    solve_puzzle(algorithm, state.State(board, empty_space))





if __name__ == "__main__":
    argv = sys.argv

    config_file: str = 'config.json'
    if len(argv) > 1:
        config_file = argv[1]

    try:
        main(config_file)
    except FileNotFoundError:
        print("error")


 