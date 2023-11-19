from algorithms.graph.search.breadth_first_search import BreadthFirstSearch


def test_breadth_first_search(graph):
    bfs = BreadthFirstSearch(graph)
    found_vertices = bfs.execute(0)
    assert [0, 1, 3, 2, 4] == found_vertices
