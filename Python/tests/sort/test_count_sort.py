import pytest

from tests.sort.resources.sort_data import test_data
from algorithms.sort.counting_sort import CountingSort

@pytest.mark.parametrize("to_sort,expected", test_data)
def test_given_heap_sort_array_return_sorted_array(to_sort, expected) -> None:
    sorted_values = CountingSort.sort(to_sort)
    assert expected == sorted_values
