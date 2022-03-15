
from classes.state import State


class Node:
  def __init__(self, parent, state: State):
    self.state = state
    self.parent = parent
    if(self.parent is None):
      self.depth = 0
    else:
      self.depth = self.parent.depth +1
  
  def __str__(self):
    return f'{self.state}'

class HeuristicNode(Node):
  def __init__(self, parent, state: State,f):
    self.state = state
    self.parent = parent
    self.f = f
    if(self.parent is None):
      self.depth = 0
    else:
      self.depth = self.parent.depth +1

  def __str__(self):
    return f'h={self.f} \n{self.state}'


  def __eq__(self, other):
    if other is None:
      return False
    return self.f == other.f
  
  def __lt__ (self, other):
    return self.f < other.f
    