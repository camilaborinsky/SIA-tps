from turtle import color
from treelib import Node, Tree
from classes.node import Node 
from pyvis.network import Network

from output.search_output import SearchOutput


def render_tree(output: SearchOutput):
    explored = output.explored_nodes.copy()
    nt = Network(height="900px", width="900px", heading=f"Nodos explotados: {output.expanded_nodes}\n Nodos frontera: {len(output.frontier_nodes)} \n Profundidad de la solución: {output.final.depth}")
    f = open('output/visualization_options.json')

    lines = f.read()
    nt.set_options(lines)
    solution = set()
    solution_node:Node = output.final
    while solution_node is not None:
        solution.add(solution_node.state)
        solution_node = solution_node.parent
    # tree = Tree()
    aux = explored.pop()
    nt.add_node(hash(aux.state), str(aux.state), color="red")
    # tree.create_node(str(aux.state.board.positions), hash(aux.state))
    while explored:
        curr_node = explored.pop()
        # tree.create_node(str(curr_node.state.board.positions), hash(curr_node.state), parent=hash(curr_node.parent.state))
        if curr_node is output.final:
            color = "red"
        elif curr_node.state in solution:
            color = "green"
        else:
            color = "blue"
        nt.add_node(hash(curr_node.state), str(curr_node.state), color=color)
        nt.add_edge(hash(curr_node.parent.state), hash(curr_node.state), color =color)

    # tree.show()
    nt.show("dot.html")
