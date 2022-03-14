class SearchOutput:
    def __init__(self, expanded_nodes: int, frontier_nodes:int,  found_solution: bool, solution):
        self.expanded_nodes = expanded_nodes
        self.frontier_nodes = frontier_nodes
        self.found_solution = found_solution
        self.solution = solution