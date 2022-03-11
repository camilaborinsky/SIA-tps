from classes.movement import Movement

class Point:
  def __init__(self, x:int, y:int):
    self.x = x
    self.y = y
    
  def get_movements(self, width: int, height: int):
    movements = [] #up down left right
    if(self.x < 0 or self.y < 0 or self.x >= width or self.y >= height):
      return movements
    if(self.x > 0):
      movements.append(Movement.Left)
    if(self.x < width -1):
      movements.append(Movement.Right)
    if(self.y > 0):
      movements.append(Movement.Up)
    if(self.y < height-1):
      movements.append(Movement.Down)
    return movements
    
  def move(self, movement: Movement):
    return Point(self.x + movement.value[0], self.y+movement.value[1])

  def __str__(self):
    return "Point: ( " + str(self.x) + ", " + str(self.y) + ")"