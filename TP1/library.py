import enum

class SearchAlgorithm(enum.Enum):
    'DFS',
    'BFS',
    'VDS',  #Variable Depth Search
    'PH',
    'GREEDY'
    'A*'


class Board:
    def __init__(self, positions):
        self.positions = positions  # matrix = [[0,0,0],[0,0,0],[0,0,0]]
        pass

class State:
  def __init__(self, board: Board):
    self.board: Board = board

class Node:
  def __init__(self, parent, state, depth):
    self.state: State = state
    self.parent: Node = parent
    self.depth = depth