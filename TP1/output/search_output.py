class SearchOutput:
    def __init__(self, expanded_nodes: int, frontier_nodes,  found_solution: bool, final, explored_nodes):
        self.expanded_nodes = expanded_nodes
        self.frontier_nodes = frontier_nodes
        self.found_solution = found_solution
        self.final = final
        self.explored_nodes = explored_nodes