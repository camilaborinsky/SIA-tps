from collections import deque

from classes.state import State
from classes.node import Node
from classes.board import Board




def run(init_state: State, max_depth):
    initial_node = Node(None, init_state)

    explored = deque()
    initial_node.depth = 0;
    frontier = deque()
    frontier.append(initial_node)

    expanded_count = 0

    while len(frontier)>0:
        print("entering big while")
        current_node: Node = frontier.popleft()
        while current_node.depth >= max_depth:
            print("current node exceeded depth")
            if len(frontier) == 0:
                print("No possible solution with current depth")
                return 
            current_node = frontier.popleft()

        print(current_node.state.board)
        print("expanded count: ", expanded_count)
        current_state: State = current_node.state
        current_board = current_state.board
        current_empty_space = current_state.empty_space
        print(current_board)
        if current_node not in explored:
            print("Unexplored territory!")
            explored.append(current_node)
            #Is this node the solution? 
            if current_node.state.is_final():
                print("Final solution!")
                solution = deque()
                while current_node is not None:
                    solution.appendleft(current_node)
                    current_node = current_node.parent
                return solution
            #Go on to expand current node
            expanded_count +=1
            for movement in current_node.state.empty_space.get_movements(3,3):
                print(movement)
                print("hello")
                new_board, new_empty = current_board.move(movement, current_empty_space)
                new_node = Node(current_node, State(new_board, new_empty))
                #Creo que esta linea es innecesaria por como esta definido depth en Node. 
                new_node.depth = current_node.depth+1
                print("new node depth: ", new_node.depth)
                if not new_node in frontier:
                    frontier.append(new_node)

    print("we're out!")


            




