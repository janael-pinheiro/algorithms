from dataclasses import dataclass, field
from typing import List

from algorithms.graph.search.graph import Graph


@dataclass
class DepthFirstSearch:
    graph: Graph
    found_vertices: List[int] = field(default_factory=list)

    def execute(self, vertex: int) -> List[int]:
        visited: List[bool] = [False for _ in range(self.graph.number_vertices)]
        self.__recur(vertex, visited)
        return self.found_vertices

    def __recur(self, vertex: int, visited: List[bool]):
        visited[vertex] = True
        self.found_vertices.append(vertex)

        current_adjacent_vertices = self.graph.adjacent_vertices[vertex]
        for current_vertex in current_adjacent_vertices:
            if not visited[current_vertex]:
                self.__recur(current_vertex, visited)
