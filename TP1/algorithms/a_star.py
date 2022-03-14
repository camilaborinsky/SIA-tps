from collections import Callable, deque
from classes import state,node
import copy

from classes.board import Board
from classes.heuristics import Heuristics
State = state.State
HeuristicNode = node.HeuristicNode

def g(n:HeuristicNode):
    return n.depth


def expand(node: HeuristicNode,leaf_nodes,explored,heuristic: Callable[[State], int]):
    movements = node.state.empty_space.get_movements(3,3)
    for mov in movements:
        b,p = node.state.board.move(mov,node.state.empty_space)
        n: HeuristicNode = HeuristicNode(node,State(b,p),0)
        # f(n) = g(n) + h(n.s)
        n.f = g(n) + heuristic(n.state)
        
        
        #if n.state not in explored:
        leaf_nodes.append(copy.copy(n))
        explored.append(n.state)
        
    



def run(initial_state: State,heuristic: Callable[[State], int]):

    initial_node = HeuristicNode(None, initial_state,0)
    # Crear A, F y Ex inicialmente vacios
    tree = initial_node
    leaf_nodes = deque()
    explored = deque()

    # Insertar el nodo raiz n0 en A y F
    leaf_nodes.append(initial_node)
    

    

    # Mientras F no este vacia
    while len(leaf_nodes)>0 :

        current_node: HeuristicNode = leaf_nodes.popleft()
        
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
        expand(current_node,leaf_nodes,explored,heuristic)
        # Reorder
        items = [leaf_nodes.pop() for x in range(len(leaf_nodes))]
        items.sort(key=lambda x: x.f)
        leaf_nodes = deque(items)
    
        
