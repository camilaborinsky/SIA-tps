from collections import deque

from classes.state import State
from classes.node import Node
from classes.board import Board




def find_solution(init_state: State, max_depth):
    initial_node = Node(None, init_state)

    explored = dict()
    initial_node.depth = 0;
    frontier = deque()
    frontier.append(initial_node)

    expanded_count = 0

    while len(frontier)>0:
        print("entering big while")
        current_node: Node = frontier.pop()
        while current_node.depth >= max_depth:
            print("current node exceeded max depth")
            if len(frontier) == 0:
                print("No possible solution with current")
                return 
            current_node = frontier.pop()

        print(current_node.state.board)
        print("node depth: ", current_node.depth)
        print("expanded count: ", expanded_count)
        current_state: State = current_node.state
        current_board = current_state.board
        current_empty_space = current_state.empty_space
    
        board_string = str(current_board.positions)    
        explored_value = explored.get(board_string)


        if (explored_value == None) or (explored_value != None and explored_value[1] > current_node.depth):
            print("Unexplored territory!")
            if explored_value != None and explored_value[1] > current_node.depth:
                print("previous depth: ", explored_value[1], " current depth: ", current_node.depth)

            explored_value = (current_node, current_node.depth) #the value in the dictionary is the lowest (in this case only) depth at witch this node was explored
            explored[board_string] = explored_value

            #Is this node the solution? 
            if current_node.state.is_final():
                print("Final solution!")
                solution = deque()
                while current_node is not None:
                    solution.append(current_node)
                    current_node = current_node.parent
                return solution, current_node.depth
            #Go on to expand current node
            expanded_count +=1
            for movement in current_node.state.empty_space.get_movements(3,3):
                new_board, new_empty = current_board.move(movement, current_empty_space)
                new_node = Node(current_node, State(new_board, new_empty))
                #Creo que esta linea es innecesaria por como esta definido depth en Node. 
                new_node.depth = current_node.depth+1
                if not new_node in frontier:
                    frontier.append(new_node)

    
    print("we're out!")
    return None

def run(init_state : State, initial_depth):
    previous_depth = initial_depth
    solution, depth = find_solution(init_state, initial_depth)
    
    





            




