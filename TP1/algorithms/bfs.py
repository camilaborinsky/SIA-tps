

from collections import deque
from operator import contains
import queue
from typing import Set
from constants import Movement
from classes.board import Board
from classes.point import Point
from classes.node import Node
from classes.state import State
from output.search_output import SearchOutput


def solve(initial_state: State)-> SearchOutput:
    root = Node(None, initial_state)

    explored : Set[State] = set()
    explored_nodes = deque()
    explored.add(root.state)
    explored_nodes.appendleft(root)

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
            for movement in current_empty_space.get_movements(3, 3):
                b,p = current_board.move(movement,current_empty_space)
                new_node = Node(to_expand, State(b, p)) 
                if (new_node.state not in explored):
                    to_visit.append(new_node)
                    explored.add(new_node.state)
                    explored_nodes.appendleft(new_node)
    
    if solved:
        return SearchOutput(expanded_count, len(to_visit), True, explored_nodes)
    else:
        return SearchOutput(expanded_count, len(to_visit), False, explored_nodes)
