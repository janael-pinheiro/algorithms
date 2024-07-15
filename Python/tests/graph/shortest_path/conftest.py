from pytest import fixture


@fixture(scope="module")
def directed_graph():
    return [
        [(1, 1), (2, 4)],
        [(2, 2), (3, 6)],
        [(3, 3)],
        [(4, 1)],
        [(4, 0)]
    ]
