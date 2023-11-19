from dataclasses import dataclass
from queue import Queue
from typing import List

from algorithms.graph.search.graph import Graph


@dataclass
class BreadthFirstSearch:
    graph: Graph

    def execute(self, source_vertex: int) -> List[int]:
        visited: List[bool] = [False for _ in range(self.graph.number_vertices)]
        queue = Queue(self.graph.number_vertices)
        found_vertices = []

        visited[source_vertex] = True
        queue.put(source_vertex)

        while queue.qsize() > 0:
            s = queue.get()
            found_vertices.append(s)

            adjacent_vertices = self.graph.adjacent_vertices[s]
            for vertex in adjacent_vertices:
                if not visited[vertex]:
                    visited[vertex] = True
                    queue.put(vertex)
        return found_vertices
