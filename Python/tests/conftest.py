import pytest

from algorithms.graph.search.graph import Graph
from algorithms.sort.bubble_sort import BubbleSort
from algorithms.sort.insertion_sort import InsertionSort
from algorithms.sort.merge_sort import MergeSort
from algorithms.sort.quick_sort import QuickSort
from algorithms.sort.selection_sort import SelectionSort


@pytest.fixture(scope="function")
def bubble_sort():
    return BubbleSort()


@pytest.fixture(scope="function")
def quick_sort():
    return QuickSort()


@pytest.fixture(scope="function")
def insertion_sort():
    return InsertionSort()


@pytest.fixture(scope="function")
def merge_sort():
    return MergeSort()


@pytest.fixture(scope="function")
def selection_sort():
    return SelectionSort()


@pytest.fixture(scope="function")
def graph():
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 3)

    return graph
