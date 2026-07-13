"""A small, easy-to-read directed graph.

We store the graph as a dictionary (the "adjacency list"):
    { "CS101": ["CS102"], "CS102": ["CS201"], ... }
which means "from CS101 you can go to CS102".

In USMS this models course prerequisites: an edge prereq -> course means
the prerequisite must be completed before the course.
"""


class Graph:
    # (from graph): simplified, readable implementation
    def __init__(self):
        # vertex -> list of vertices it points to
        self.adjacency_list = {}

    # ---------- building the graph ----------

    def add_vertex(self, vertex):
        """Add a point on the graph (if it isn't there already)."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination):
        """Draw an arrow from source to destination."""
        self.add_vertex(source)
        self.add_vertex(destination)
        if destination not in self.adjacency_list[source]:
            self.adjacency_list[source].append(destination)

    def remove_edge(self, source, destination):
        """Erase the arrow from source to destination."""
        if source in self.adjacency_list and destination in self.adjacency_list[source]:
            self.adjacency_list[source].remove(destination)

    def remove_vertex(self, vertex):
        """Erase a point and every arrow touching it."""
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
        for neighbors in self.adjacency_list.values():
            if vertex in neighbors:
                neighbors.remove(vertex)

    # ---------- asking questions ----------

    def get_neighbors(self, vertex):
        """Where can we go from this vertex?"""
        return self.adjacency_list.get(vertex, [])

    def has_vertex(self, vertex):
        return vertex in self.adjacency_list

    def has_edge(self, source, destination):
        return destination in self.adjacency_list.get(source, [])

    def get_vertices(self):
        return list(self.adjacency_list.keys())

    def get_edges(self):
        edges = []
        for source, neighbors in self.adjacency_list.items():
            for destination in neighbors:
                edges.append((source, destination))
        return edges

    def indegree(self, vertex):
        """How many arrows point AT this vertex."""
        return sum(1 for neighbors in self.adjacency_list.values() if vertex in neighbors)

    def is_reachable(self, start, target):
        """Can we walk from start to target following the arrows?"""
        if start == target:
            return True

        visited = set()
        frontier = [start]          # places we still need to look at
        while frontier:
            current = frontier.pop()
            if current == target:
                return True
            if current in visited:
                continue
            visited.add(current)
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in visited:
                    frontier.append(neighbor)
        return False

    def has_cycle(self):
        """Is there a loop of arrows that leads back to where it started?"""
        visited = set()        # every vertex we've fully checked
        in_path = set()        # vertices on the current walk

        def walk(vertex):
            visited.add(vertex)
            in_path.add(vertex)
            for neighbor in self.adjacency_list.get(vertex, []):
                if neighbor in in_path:
                    return True     # we looped back -> cycle!
                if neighbor not in visited and walk(neighbor):
                    return True
            in_path.discard(vertex)
            return False

        for vertex in self.adjacency_list:
            if vertex not in visited and walk(vertex):
                return True
        return False

    def topological_sort(self):
        """Order vertices so every arrow goes left-to-right.

        Returns a list, or None if the graph has a cycle (no order possible).
        """
        # Count how many arrows point at each vertex.
        pending = {v: self.indegree(v) for v in self.adjacency_list}

        # Start with the vertices that nothing points to.
        ready = [v for v in pending if pending[v] == 0]
        order = []

        while ready:
            current = ready.pop()
            order.append(current)
            for neighbor in self.adjacency_list.get(current, []):
                pending[neighbor] -= 1
                if pending[neighbor] == 0:
                    ready.append(neighbor)

        # If we couldn't place every vertex, there must be a cycle.
        return order if len(order) == len(pending) else None

    # ---------- helpers ----------

    def __str__(self):
        lines = []
        for source in sorted(self.adjacency_list.keys()):
            targets = self.adjacency_list[source]
            lines.append(f"{source} -> {', '.join(targets) if targets else '(none)'}")  # (changed): ASCII-safe for Windows
        return "\n".join(lines)

