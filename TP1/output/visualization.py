from treelib import Node, Tree
from classes.node import Node 


def render_tree( explored):
    tree = Tree()
    aux = explored.pop()
    tree.create_node(str(aux.state.board.positions), hash(aux.state))
    while explored:
        curr_node = explored.pop()
        tree.create_node(str(curr_node.state.board.positions), hash(curr_node.state), parent=hash(curr_node.parent.state))

    tree.show()
