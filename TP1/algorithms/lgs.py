
from collections import deque
from typing import Callable
from classes.node import Node
from classes.heuristics import Heuristics
from classes.state import State


def solve(initial_state:State, heuristic: Callable[[State], int]):
    root = Node(None, initial_state)

    explored = {}
    explored[root] = True

    to_visit = deque()
    to_visit.append(root)

    solved = False
    expanded_count = 0
