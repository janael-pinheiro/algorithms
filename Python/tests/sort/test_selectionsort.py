import pytest

from tests.sort.resources.sort_data import test_data
from algorithms.sort.selection_sort import SelectionSort


@pytest.mark.parametrize("to_sort,expected", test_data)
def test_given_selection_sort_array_return_sorted_array(selection_sort, to_sort, expected) -> None:
    sorted_values = SelectionSort.sort(to_sort)
    assert expected == sorted_values
