

from utils import count_inversions
from classes.board import Board
from classes.point import Point


class State:
  def __init__(self, board: Board, empty_space: Point):
    self.board = board
    self.empty_space = empty_space

  def is_final(self):
    for idx, val in enumerate(self.board.positions):
        if (idx+1 < 9 and val != idx+1) or (idx+1 == 9 and val != 0):
          return False
    return True

  def is_solvable(self):
    return count_inversions(self.board.positions, len(self.board.positions)) % 2 == 0

  def __eq__(self, other):
        return self.__hash__ == other.__hash__

  def __hash__(self):
        return hash(str(frozenset(self.board.positions)))
  

