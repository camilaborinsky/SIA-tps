
from classes.state import State


class Node:
  def __init__(self, parent, state: State, depth):
    self.state = state
    self.parent = parent
    self.depth = depth