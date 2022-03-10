
from classes.state import State


class Heuristics:
    def __init__(self) -> None:
        pass

    def hamming(self, state: State):
        i = 0
        for idx, val in enumerate(state.board.positions):
            print(idx, val)
            if val != 0 and (idx+1 < 9 and val != idx+1):
                i+=1
        return i
    
    def manhattan(self, state:State):
        sum = 0
        for idx, val in enumerate(state.board.positions):
            if val != 0:
                target_pos_y = (val-1) % 3
                target_pos_x = (val-1) / 3
                current_pos_y = (idx-1) % 3
                current_pos_x = (idx-1) / 3
                sum += abs(target_pos_x - current_pos_x) + abs(target_pos_y-current_pos_y)
        return sum

    # def inversions(self, state:State):
    #     count = 0
    #     for idx, val in enumerate(state.board.positions):
    #         if(val != 0):



