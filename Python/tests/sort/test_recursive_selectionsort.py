import pytest

from tests.sort.resources.sort_data import test_data
from algorithms.sort.recursive_selectionsort import RecursiveSelectionSort


@pytest.mark.parametrize("to_sort,expected", test_data)
def test_given_recursive_selection_sort_array_return_sorted_array(to_sort, expected) -> None:
    sorted_values = RecursiveSelectionSort.sort(to_sort)
    assert expected == sorted_values
