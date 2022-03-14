
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
    aux = list(filter( lambda v: v != 0, self.board.positions))
    return count_inversions(aux, len(aux)) % 2 == 0

  def __eq__(self, other):
        return hash(self) == hash(other)

  def __hash__(self):
        return hash(tuple(self.board.positions))

  def __str__(self):
    arr = self.board.positions
    return f"{arr[0]} {arr[1]} {arr[2]}\n {arr[3]} {arr[4]} {arr[5]}\n {arr[6]} {arr[7]} {arr[8]}\n"

  

