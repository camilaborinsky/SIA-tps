from treelib import Node, Tree
from classes.node import Node 


def render_tree( explored):
    tree = Tree()
    aux = explored.pop()
    print(len(explored))
    tree.create_node(str(aux.state.board.positions), str(aux.state.board.positions))
    while explored:
        curr_node = explored.pop()
        print(len(explored))
        tree.create_node(str(curr_node.state.board.positions), str(curr_node.state.board.positions), parent=str(curr_node.parent.state.board.positions))

    tree.show()
