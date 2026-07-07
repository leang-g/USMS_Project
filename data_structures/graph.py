"""Graph implementation for prerequisites and attendance relationships."""


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list.setdefault(vertex, [])

    def add_edge(self, source, destination):
        self.add_vertex(source)
        self.add_vertex(destination)
        self.adjacency_list[source].append(destination)

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])
