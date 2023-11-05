from algorithms.sort.bubble_sort import BubbleSort
from algorithms.sort.quick_sort import QuickSort
from algorithms.sort.insertion_sort import InsertionSort
from algorithms.sort.merge_sort import MergeSort
from algorithms.sort.selection_sort import  SelectionSort

import pytest


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
