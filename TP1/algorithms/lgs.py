
from collections import deque
from typing import Callable
from classes.node import Node
from classes.heuristics import Heuristics
from classes.state import State
from typing import Set

from output.search_output import SearchOutput


def solve(initial_state:State, heuristic: Heuristics)-> SearchOutput:
    root = Node(None, initial_state)

    explored = Set[State]
    explored.add(root)

    to_expand = deque()
    to_expand.appendleft(root)

    solved = False
    expanded_count = 0

    while explored:
        current_node: Node = to_expand.popleft()
        current_state = current_node.state
        current_board = current_state.board
        current_empty_space = current_state.empty_space

        if current_state.is_final:
            solved = True
            break
        else: 
            expanded_count +=1
            new_nodes = filter(lambda node:(node.state not in explored), map(lambda movement: (Node(to_expand, State(current_board.move(movement, current_empty_space), current_empty_space.move(movement)))), current_empty_space.get_movements()))
            for n in new_nodes:
                to_expand.appendleft(n)
            
    if solved:
        return True, initial_state, current_state, expanded_count
    else:
        return False, initial_state, current_state, expanded_count

