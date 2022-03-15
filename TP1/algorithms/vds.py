from collections import deque
from typing import final

from classes.state import State
from classes.node import Node
from classes.board import Board

from output.search_output import SearchOutput
from typing import Set

import math
import copy


def find_solution(init_state: State, max_depth):
    initial_node = Node(None, init_state)
    initial_node.depth = 0;
    initial_board = str(initial_node.state.board.positions)

    explored = dict()
    explored[initial_node.state] = initial_node.depth
    
    frontier = deque()
    frontier.append(initial_node)

    explored_nodes = deque()
    explored_nodes.appendleft(initial_node)

    expanded_count = 0

    while len(frontier) > 0:
        current_node:Node = frontier.pop()
        while current_node.depth >= max_depth:
            if len(frontier) == 0:
                return SearchOutput(expanded_count, frontier, False, None, explored_nodes)
            current_node =frontier.pop()

        current_state:State = current_node.state
        current_board = current_state.board
        current_empty_space = current_state.empty_space

        if current_node.state.is_final():
            final_depth = current_node.depth
            solution = deque()
            solution_node = current_node
            while current_node is not None:
                solution.append(current_node)
                current_node = current_node.parent
            return SearchOutput(expanded_count, frontier, True, solution_node, explored_nodes)

        else: 
            expanded_count +=1
            for movement in current_node.state.empty_space.get_movements(3,3):
                new_board, new_empty = current_board.move(movement, current_empty_space)
                new_node = Node(current_node, State(new_board, new_empty))
                new_node.depth = current_node.depth+1
                explored_value = explored.get(new_node.state)
                if (explored_value == None) or (explored_value > current_node.depth):
                    frontier.append(new_node)
                    explored_nodes.appendleft(new_node)
                    explored[new_node.state] = new_node.depth

    return SearchOutput(expanded_count, frontier, False, None, explored_nodes)





def solve(init_state : State, initial_depth):
    print("Tried to solve with depth: ", initial_depth, end='')
    previous_depth = 0
    new_depth = initial_depth
    search_output: SearchOutput = find_solution(init_state, initial_depth)
    
    #busco la primer cota superior
    while search_output.found_solution == False:
        previous_depth = new_depth
        new_depth = previous_depth+10
        search_output = find_solution(init_state, new_depth)

    
    lower_bound = previous_depth #ultima profundidad a la que no consegui solucion
    upper_bound = search_output.final.depth # primer profundidad a la que consegui solucion
 
    last_successful_output = search_output
    
    while upper_bound - lower_bound > 1:
        mid_point = math.trunc((lower_bound+upper_bound)/2)
        print(", ", mid_point, end='')
        search_output = find_solution(init_state, mid_point)
        if search_output.found_solution == False: #midpoint doesnt find solutions, midpoint becomes new lower bound
            if lower_bound == mid_point: #last case where lower_bound and upper bound are split by one number
                return last_successful_output
            lower_bound = mid_point
        else: #midpoint finds solution, found depthbecomes new upper bound
            upper_bound = search_output.final.depth
            last_successful_output = search_output
    print("optimal depth: ", upper_bound)
    return last_successful_output

            



    
    





            




