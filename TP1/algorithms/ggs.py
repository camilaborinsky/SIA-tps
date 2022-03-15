
from classes.node import Node, HeuristicNode
from classes.heuristics import Heuristics
from classes.state import State

from typing import Set
import heapq
from collections import deque

from output.search_output import SearchOutput

def solve(initial_state:State, heuristic: Heuristics)-> SearchOutput:
    root = HeuristicNode(None, initial_state, heuristic.calculate(initial_state))

    explored: Set[State] = set()
    explored.add(root.state)

    frontier = []
    heapq.heappush(frontier, root)

    #variables relevant for output
    solved = False
    expanded_count = 0
    explored_nodes = deque()
    explored_nodes.appendleft(root)
    

    while len(frontier) != 0:
        current_node: HeuristicNode = heapq.heappop(frontier)
        current_state = current_node.state
        current_board = current_state.board
        current_empty_space = current_state.empty_space

        if current_state.is_final():
            solved = True
            break 
        else:
            expanded_count +=1
            for movement in current_empty_space.get_movements(3,3):
                b,p = current_board.move(movement, current_empty_space)
                aux_state = State(b,p)
                heuristic_node: HeuristicNode = HeuristicNode(current_node, aux_state, heuristic.calculate(aux_state))
                if aux_state not in explored: 
                    heapq.heappush(frontier, heuristic_node)
                    explored.add(aux_state)
                    explored_nodes.appendleft(heuristic_node)
    
    if solved:
        return SearchOutput(expanded_count, frontier, True, current_node, explored_nodes)
    else: 
        return SearchOutput(expanded_count, frontier, False, None, explored_nodes)
            
            
