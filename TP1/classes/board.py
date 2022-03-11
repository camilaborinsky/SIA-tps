from classes.point import Point
from classes.movement import Movement


class Board:
  def __init__(self, positions):
      self.positions = positions  # matrix = [[0,0,0],[0,0,0],[0,0,0]]

  def move(self, movement:Movement, empty: Point):
      move_from = empty.y*3+ empty.x
      move_to = (empty.y + movement.value[1])*3+ empty.x+movement.value[0]
      new_board = self.positions.copy()
      new_board[move_from] = new_board[move_to]
      new_board[move_to] = 0
      return new_board


  def __str__(self):
      return "Board: "+ self.positions