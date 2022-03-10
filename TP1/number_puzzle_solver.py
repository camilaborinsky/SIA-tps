from classes.search_algorithm import SearchAlgorithm
from classes import board, point, state, node, movement

import time


def solve_puzzle(algorithm: SearchAlgorithm, initial_state:state.State):
    #start timer
    initial_timestamp = time.time()
    print("Starting algorithm ", algorithm)
    # call solve method for corresponding algorithm
    p1 = point.Point(3,3)
    print(p1.get_movements(3,3))
    p1.move(movement.Movement.Right)
    print(p1)

    #end timer
    final_timestamp = time.time()
    print("Processing time: ", final_timestamp - initial_timestamp)
    #print metrics


board = board.Board([[1,2,3],[5,4,7],[6,8,0]])
empty_space = point.Point(2,2)
solve_puzzle("BFS", state.State(board, empty_space))

