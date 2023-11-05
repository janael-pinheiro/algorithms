import pytest

from tests.sort.resources.sort_data import test_data
from algorithms.sort.merge_sort import MergeSort


@pytest.mark.parametrize("to_sort,expected", test_data)
def test_given_merge_sort_array_return_sorted_array(merge_sort, to_sort, expected) -> None:
    sorted_values = MergeSort.sort(to_sort, 0, len(to_sort) - 1)
    assert expected == sorted_values
