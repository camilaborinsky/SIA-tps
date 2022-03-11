import enum 

class Movement(enum.Enum):
   Up = [0, -1]
   Down = [0, 1]
   Left = [-1, 0]
   Right = [1, 0]
