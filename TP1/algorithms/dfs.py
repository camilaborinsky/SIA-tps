from collections import deque
from classes import state,node
import copy

from classes.board import Board
from output.search_output import SearchOutput
Node  = node.Node
State = state.State


def expand(node: Node,leaf_nodes,explored):
    movements = node.state.empty_space.get_movements(3,3)
    for mov in movements:
        b,p = node.state.board.move(mov,node.state.empty_space)
        n: Node = Node(node,State(b,p))

        if n.state not in explored:
            leaf_nodes.appendleft(copy.copy(n))
            explored.append(n.state)
    



def solve(initial_state: State) -> SearchOutput:

    initial_node = Node(None, initial_state)

    tree = initial_node
    leaf_nodes = deque()
    explored = deque()

    
    leaf_nodes.append(initial_node)


    while len(leaf_nodes)>0 :

        current_node: Node = leaf_nodes.popleft()
        if current_node.state not in explored:
            explored.append(current_node.state)
        # Check if current node has an objective state
        if current_node.state.is_final():
            print("Finalized")
            solution  = deque()
            while current_node is not None:
                solution.appendleft(current_node)
                current_node = current_node.parent
            return solution
        # Expand current node
        expand(current_node,leaf_nodes,explored)
          

