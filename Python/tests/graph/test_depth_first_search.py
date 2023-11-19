from algorithms.graph.search.depth_first_search import DepthFirstSearch


def test_depth_first_search(graph):
    bfs = DepthFirstSearch(graph)
    found_vertices = bfs.execute(0)
    assert [0, 1, 3, 2, 4] == found_vertices
