import pytest

from tests.sort.resources.sort_data import test_data

@pytest.mark.parametrize("to_sort,expected", test_data)
def test_given_quick_sort_array_return_sorted_array(quick_sort, to_sort, expected) -> None:
    left: int = 0
    right: int = len(to_sort) - 1
    sorted_values = quick_sort.sort(to_sort, left, right)
    assert expected == sorted_values
