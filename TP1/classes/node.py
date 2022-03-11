
from classes.state import State


class Node:
  def __init__(self, parent, state: State):
    self.state = state
    self.parent = parent
    if(self.parent is None):
      self.depth = 0
    else:
      self.depth = self.parent.depth +1
    