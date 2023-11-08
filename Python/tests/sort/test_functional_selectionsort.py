import pytest

from tests.sort.resources.sort_data import test_data
from algorithms.sort.functional_selectionsort import FunctionalSelectionSort


@pytest.mark.parametrize("to_sort,expected", test_data)
def test_given_functional_selection_sort_array_return_sorted_array(to_sort, expected) -> None:
    sorted_values = FunctionalSelectionSort.sort(zip(range(len(to_sort)), to_sort))
    assert expected == sorted_values
