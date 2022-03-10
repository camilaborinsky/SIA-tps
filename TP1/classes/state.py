

from classes.board import Board
from classes.point import Point


class State:
  def __init__(self, board: Board, empty_space: Point):
    self.board = board
    self.empty_space = empty_space

  def is_final(self):
    for idx, val in enumerate(self.board.positions):
        print(idx, val)
        if (idx+1 < 9 and val != idx+1) or (idx+1 == 9 and val != 0):
          return False
    return True
    