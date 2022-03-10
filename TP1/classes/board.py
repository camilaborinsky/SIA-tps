class Board:
  def __init__(self, positions):
      self.positions = positions  # matrix = [[0,0,0],[0,0,0],[0,0,0]]

  def __str__(self):
      return "Board: "+ self.positions