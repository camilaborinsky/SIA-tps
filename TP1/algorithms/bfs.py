

from collections import deque
import queue
from typing import Set
from classes.board import Board
from classes.point import Point
from classes.node import Node
from classes.state import State


def solve(initial_state: State):
    root = Node(None, initial_state)

    explored = Set[State]
    explored.add(root)

    to_visit = deque()
    to_visit.append(root)

    solved = False
    expanded_count = 0

    while to_visit:
        to_expand: Node = to_visit.popleft()
        current_state: State = to_expand.state
        current_empty_space: Point = current_state.empty_space
        current_board: Board = current_state.board

        if(current_state.is_final()):
            solved= True
            break
        else:
            expanded_count +=1
            for movement in current_empty_space.get_movements():
                new_node = Node(to_expand, State(current_board.move(movement, current_empty_space)))
                if not new_node in explored:
                    to_visit.append(new_node)
                    explored.add(new_node)
    
    if solved:
        return True, initial_state, current_state, expanded_count
    else:
        return False, initial_state, current_state, expanded_count
