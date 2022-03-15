from collections import deque
from classes import state,node
import copy

from classes.board import Board
from output.search_output import SearchOutput
Node  = node.Node
State = state.State


def expand(node: Node,leaf_nodes,explored,explored_nodes):
    movements = node.state.empty_space.get_movements(3,3)
    for mov in movements:
        b,p = node.state.board.move(mov,node.state.empty_space)
        n: Node = Node(node,State(b,p))

        current_board = str(n.state.board.positions)
        if explored.get(current_board) == None:
            leaf_nodes.appendleft(copy.copy(n))
            explored[current_board] = copy.copy(n)
            explored_nodes.appendleft(copy.copy(n))
    



def solve(initial_state: State) -> SearchOutput:

    initial_node = Node(None, initial_state)

    tree = initial_node
    leaf_nodes = deque()
    explored = dict()
    expanded_count = 0
    explored_nodes = deque()
    explored_nodes.appendleft(initial_node)

    
    leaf_nodes.append(initial_node)


    while len(leaf_nodes)>0 :

        current_node: Node = leaf_nodes.popleft()
        current_board = str(current_node.state.board.positions)
        if explored.get(current_board) == None:
            explored[current_board] = current_node
        # Check if current node has an objective state
        if current_node.state.is_final():
            print("Finalized")
            return SearchOutput(expanded_count, leaf_nodes, True, current_node, explored_nodes)
            
        # Expand current node
        expanded_count += 1
        expand(current_node,leaf_nodes,explored,explored_nodes)
    return SearchOutput(expanded_count, leaf_nodes, False, None, explored_nodes)