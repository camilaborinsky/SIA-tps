import enum


class ConfigParams(enum.Enum):
    ALGORITHM="algorithm"
    HEURISTIC="heuristic"
    BOARD="board"

    def __str__(self) -> str:
        return self.value


class Movement(enum.Enum):
   Up = [0, -1]
   Down = [0, 1]
   Left = [-1, 0]
   Right = [1, 0]

class Heuristic(enum.Enum):
    hamming = 'hamming'
    manhattan = 'manhattan'
    inversions = 'inversions'


class SearchAlgorithm(enum.Enum):
    DFS = 'DFS'
    BFS = 'BFS'
    VDS = 'VDS'  #Variable Depth Search
    GGS = 'GGS'  #Global greedy search
    LGS = 'LGS'   #Local greedy search
    A_STAR = 'A*'