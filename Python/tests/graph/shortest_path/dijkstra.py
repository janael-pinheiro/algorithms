from algorithms.graphs.shortest_path.dijkstra import Dijkstra


def test_dijkstra_shortest_path(directed_graph):
    dijkstra = Dijkstra(directed_graph)
    expected_output = [0, 1, 3, 6, 7]
    output = dijkstra.execute(0)
    assert expected_output == output
