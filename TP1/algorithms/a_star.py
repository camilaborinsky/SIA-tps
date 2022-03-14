from collections import Callable, deque
from classes import state,node
import copy

from classes.board import Board
from classes.heuristics import Heuristics
from output.search_output import SearchOutput
State = state.State
HeuristicNode = node.HeuristicNode

def g(n:HeuristicNode):
    return n.depth


def expand(node: HeuristicNode,leaf_nodes,explored,heuristic: Heuristics):
    movements = node.state.empty_space.get_movements(3,3)
    for mov in movements:
        b,p = node.state.board.move(mov,node.state.empty_space)
        n: HeuristicNode = HeuristicNode(node,State(b,p),0)
        # f(n) = g(n) + h(n.s)
        n.f = g(n) + heuristic.calculate(n.state)
        
        current_board = str(n.state.board.positions)
        if explored.get(current_board) == None:
            leaf_nodes.append(copy.copy(n))
            explored[current_board] = n
        
        
    



def solve(initial_state: State,heuristic: Heuristics)-> SearchOutput:

    initial_node = HeuristicNode(None, initial_state,0)
    # Crear A, F inicialmente vacios
    tree = initial_node
    leaf_nodes = list()
    explored = dict()

    # Insertar el nodo raiz n0 en A y F
    leaf_nodes.append(initial_node)
    

    

    # Mientras F no este vacia
    while len(leaf_nodes)>0 :

        current_node: HeuristicNode = leaf_nodes.pop()
        current_board = str(current_node.state.board.positions)
        if explored.get(current_board) == None:
            explored[current_board] = current_node
        # Check if current node has an objective state
        if current_node.state.is_final():
            print("Finalized")
            solution  = deque()
            while current_node is not None:
                solution.appendleft(current_node)
                current_node = current_node.parent
            return solution
        # Expand current node
        expand(current_node,leaf_nodes,explored,heuristic)
        # Reorder
        leaf_nodes.sort(key=lambda x: x.f, reverse = True)
    
        
