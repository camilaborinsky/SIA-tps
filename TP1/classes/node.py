
from classes.state import State


class Node:
  def __init__(self, parent, state: State):
    self.state = state
    self.parent = parent
    if(self.parent is None):
      self.depth = 0
    else:
      self.depth = self.parent.depth +1

class HeuristicNode(Node):
  def __init__(self, parent, state: State,f):
    self.state = state
    self.parent = parent
    self.f = f
    if(self.parent is None):
      self.depth = 0
    else:
      self.depth = self.parent.depth +1
  
  def __lt__ (self, other):
    return self.f < other.f
    