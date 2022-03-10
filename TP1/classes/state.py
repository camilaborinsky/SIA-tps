

from classes.board import Board
from classes.point import Point


class State:
  def __init__(self, board: Board, empty_space: Point):
    self.board = board
    self.empty_space = empty_space