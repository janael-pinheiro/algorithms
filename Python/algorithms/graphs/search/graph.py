from dataclasses import dataclass, field
from typing import List


@dataclass
class Graph:
    number_vertices: int
    adjacent_vertices: List[List[int]] = field(default_factory=list)

    def __post_init__(self):
        for _ in range(self.number_vertices):
            self.adjacent_vertices.append(list())

    def add_edge(self, v: int, w: int):
        self.adjacent_vertices[v].append(w)
