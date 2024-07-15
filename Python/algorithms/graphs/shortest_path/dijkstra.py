import sys
from dataclasses import dataclass, field
from typing import List, Tuple, Set, Union
from heapq import heappush, heappop


@dataclass
class Dijkstra:
    graph: List[List[Tuple[int, int]]]
    __heap: List[Tuple[int, int]] = field(default_factory=list)
    __found_vertices: Set[int] = field(default_factory=set)

    def execute(self, source: int) -> List[int]:
        shortest_paths = [sys.maxsize for _ in range(len(self.graph))]
        shortest_paths[source] = 0
        self.__found_vertices.add(source)
        current_vertex = source
        while True:
            selected_vertex, minimum_cost =\
                self.__find_minimum_cost_edge(current_vertex)
            if selected_vertex is None:
                break
            shortest_paths[selected_vertex] =\
                shortest_paths[current_vertex] + minimum_cost
            current_vertex = selected_vertex
        return shortest_paths

    def __find_minimum_cost_edge(
            self,
            current_vertex: int) -> Union[Tuple[int, int], Tuple[None, None]]:
        if len(self.graph[current_vertex]) == 1 and self.graph[current_vertex][0][0] == current_vertex:
            return None, None
        for vertex in self.graph[current_vertex]:
            heappush(self.__heap, (vertex[1], vertex[0]))
        selected_vertex = heappop(self.__heap)
        if selected_vertex in self.__found_vertices:
            self.__find_minimum_cost_edge(current_vertex)
        return selected_vertex[1], selected_vertex[0]
