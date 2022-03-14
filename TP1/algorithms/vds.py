from collections import deque

from classes.state import State
from classes.node import Node
from classes.board import Board

import math




def find_solution(init_state: State, max_depth):
    initial_node = Node(None, init_state)

    explored = dict()
    initial_node.depth = 0;
    frontier = deque()
    frontier.append(initial_node)

    expanded_count = 0

    while len(frontier)>0:
        current_node: Node = frontier.pop()
        while current_node.depth >= max_depth:
            if len(frontier) == 0:
                print("No possible solution with current depth")
                return None, -1
            current_node = frontier.pop()

        current_state: State = current_node.state
        current_board = current_state.board
        current_empty_space = current_state.empty_space
    
        board_string = str(current_board.positions)    
        explored_value = explored.get(board_string)


        if (explored_value == None) or (explored_value != None and explored_value[1] > current_node.depth):

            explored_value = (current_node, current_node.depth) #the value in the dictionary is the lowest (in this case only) depth at witch this node was explored
            explored[board_string] = explored_value

            #Is this node the solution? 
            if current_node.state.is_final():
                print("Solution found!")
                print(current_node.state.board)
                final_depth = current_node.depth
                print("Profundidad: ", final_depth, "Con profundidad maxima: ", max_depth)
                solution = deque()
                while current_node is not None:
                    solution.append(current_node)
                    current_node = current_node.parent
                return solution, final_depth
            #Go on to expand current node
            expanded_count +=1
            for movement in current_node.state.empty_space.get_movements(3,3):
                new_board, new_empty = current_board.move(movement, current_empty_space)
                new_node = Node(current_node, State(new_board, new_empty))
                #Creo que esta linea es innecesaria por como esta definido depth en Node. 
                new_node.depth = current_node.depth+1
                if not new_node in frontier:
                    frontier.append(new_node)

    
    print("we're out!")
    return None, -1

def run(init_state : State, initial_depth):
    previous_depth = 0
    new_depth = initial_depth
    solution, depth = find_solution(init_state, initial_depth)
    
    #busco la primer cota superior
    while depth == -1:
        previous_depth = new_depth
        new_depth = previous_depth+10
        print("about to try with depth: ", new_depth)
        solution, depth = find_solution(init_state, new_depth)

    lower_bound = previous_depth #ultima profundidad a la que no consegui solucion
    upper_bound = depth # primer profundidad a la que consegui solucion
 

    print("Tengo cota inferior: ", lower_bound, " y cota superior: ", upper_bound)

    
    while upper_bound - lower_bound > 1:
        mid_point = math.trunc((lower_bound+upper_bound)/2)
        print("about to try with depth: ", mid_point)
        solution, depth = find_solution(init_state, mid_point)
        if depth == -1: #midpoint doesnt find solutions, midpoint becomes new lower bound
            if lower_bound == mid_point: #last case where lower_bound and upper bound are split by one number
                return solution
            lower_bound = mid_point
        else: #midpoint finds solution, found depthbecomes new upper bound
            upper_bound = depth
    print("La solucion se obtiene de manera optima con la profundidad ", upper_bound)
    return solution

            



    
    





            




