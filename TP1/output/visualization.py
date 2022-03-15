from algorithms.a_star import HeuristicNode
from classes.node import Node 
from pyvis.network import Network
from config_parser import Config

from output.search_output import SearchOutput

def render_stats(output:SearchOutput, time_diff):
    if output.found_solution:
        print("Solución encontrada\n")
        print(f"Nodos expandidos: {output.expanded_nodes}\n")
        print(f"Nodos frontera: {len(output.frontier_nodes)}\n")
        print(f"Tiempo de ejecución: {time_diff}\n")
        print(f"Profundidad de solución: {output.final.depth}\n")
        print(f"Costo de la solución: {output.final.depth}\n")
    else:
        print("No se encontró solución\n")
        print(f"Nodos expandidos: {output.expanded_nodes}\n")
        print(f"Nodos frontera: {len(output.frontier_nodes)}\n")

def render_tree(output: SearchOutput):
    explored = output.explored_nodes.copy()
    nt = Network(height="900px", width="900px", heading=f"Árbol de búsqueda")
    f = open('output/visualization_options.json')

    lines = f.read()
    nt.set_options(lines)
    solution = set()
    solution_node:Node = output.final
    while solution_node is not None:
        solution.add(solution_node.state)
        solution_node = solution_node.parent
    aux = explored.pop()
    nt.add_node(hash(aux.state), str(aux), color="#fa9a82")


    while explored:
        curr_node = explored.pop()
        if len(output.explored_nodes) <= 20000 or curr_node.state in solution:
            if curr_node is output.final:
                color = "#fa9a82"
            elif curr_node.state in solution:
                color = "#fcd874"
            else:
                color = "#827c7a"
            nt.add_node(hash(curr_node.state), str(curr_node), color=color)
            nt.add_edge(hash(curr_node.parent.state), hash(curr_node.state), color=color)

    nt.show("dot.html")

def render_config(config: Config):
    print(f"Configuración:\nEstado inicial: \n{config.board}\nAlgoritmo elegido: {config.algorithm}\n")
    if config.heuristic is not None:
        print(f"Heurística elegida: {config.heuristic}\n")
