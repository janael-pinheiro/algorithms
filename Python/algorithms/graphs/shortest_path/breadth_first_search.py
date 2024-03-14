from dataclasses import dataclass, field
from queue import Queue
from typing import List

from algorithms.graphs.search.graph import Graph


@dataclass
class BreadthFirstShortestPath:
    graph: Graph
    found_vertices: List[int] = field(default_factory=list)

    def execute(self, source_vertex: int) -> List[int]:
        visited: List[bool] = [False for _ in range(self.graph.number_vertices)]
        distances: List[int] = [-1 for _ in range(self.graph.number_vertices)]
        distances[source_vertex] = 0

        queue = Queue(self.graph.number_vertices)

        visited[source_vertex] = True
        queue.put(source_vertex)

        while queue.qsize() > 0:
            s = queue.get()
            self.found_vertices.append(s)

            adjacent_vertices = self.graph.adjacent_vertices[s]
            for vertex in adjacent_vertices:
                if not visited[vertex]:
                    visited[vertex] = True
                    distances[vertex] = distances[s] + 1
                    queue.put(vertex)
        return distances
