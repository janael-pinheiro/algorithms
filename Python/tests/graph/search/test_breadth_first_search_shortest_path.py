from algorithms.graphs.shortest_path.breadth_first_search import BreadthFirstShortestPath


def test_breadth_first_search_shortest_path(graph):
    bfs = BreadthFirstShortestPath(graph)
    distances = bfs.execute(0)
    expected = [0, 1, 1, 1, 2]
    assert expected == distances
