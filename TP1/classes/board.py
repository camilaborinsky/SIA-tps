from classes.point import Point
from constants import Movement


class Board:
  def __init__(self, positions):
      self.positions = positions  # matrix = [[0,0,0],[0,0,0],[0,0,0]]

  def move(self, movement:Movement, empty: Point):
      move_from: int = empty.y*3+ empty.x
      move_to: int = (empty.y + movement.value[1])*3+ empty.x+movement.value[0]
      new_board = self.positions.copy()
      new_board[move_from] = new_board[move_to]
      new_board[move_to] = 0
      return Board(new_board),empty.move(movement)


  def __str__(self):
      return "Board: "+ str(self.positions)

  def __eq__(self, other):
      if isinstance(other, Board):
        return hash(self) == hash(other)
      return False

  def __hash__(self):
        return hash(tuple(self.positions))