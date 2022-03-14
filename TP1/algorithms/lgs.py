
from collections import deque
from typing import Callable
from classes.node import Node, HeuristicNode
from classes.heuristics import Heuristics
from classes.state import State
from typing import Set

from output.search_output import SearchOutput


def solve(initial_state:State, heuristic: Heuristics)-> SearchOutput:
    
    root = HeuristicNode(None, initial_state, heuristic.calculate(initial_state))

    explored: Set[State] = set() 
    explored.add(root.state)
    explored_nodes = deque()
    explored_nodes.appendleft(root)

    to_expand = deque()
    to_expand.appendleft(root)

    solved = False
    expanded_count = 0

    while to_expand:
        current_node: HeuristicNode = to_expand.popleft()
        current_state = current_node.state
        current_board = current_state.board
        current_empty_space = current_state.empty_space

        if current_state.is_final():
            solved = True
            break
        else: 
            expanded_count +=1
            aux_nodes = list()
            for movement in current_empty_space.get_movements(3, 3):
                b, p = current_board.move(movement, current_empty_space)
                aux_state = State(b, p)
                aux_nodes.append(HeuristicNode(current_node, aux_state, heuristic.calculate(aux_state)))
            new_nodes = list(filter(lambda node:(node.state not in explored), aux_nodes ))
            new_nodes.sort(key=lambda n: n.f, reverse=True)
            for n in new_nodes:
                to_expand.appendleft(n)
                explored.add(n.state)
                explored_nodes.appendleft(n)
            
    if solved:
        return SearchOutput(expanded_count, to_expand, True, current_node, explored_nodes)
    else:
        return SearchOutput(expanded_count, to_expand, False, None, explored_nodes)

