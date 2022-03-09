from TP1.library import SearchAlgorithm, State

import time


def solve_puzzle(algorithm: SearchAlgorithm, initial_state:State):
    #start timer
    initial_timestamp = time.time()
    print("Starting algorithm ", algorithm)
    # call solve method for corresponding algorithm

    #end timer
    final_timestamp = time.time()
    print("Processing time: ", final_timestamp - initial_timestamp)
    #print metrics



