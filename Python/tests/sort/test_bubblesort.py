import pytest

from tests.sort.resources.sort_data import test_data

@pytest.mark.parametrize("to_sort,expected", test_data)
def test_given_bubble_sort_array_return_sorted_array(bubble_sort, to_sort, expected) -> None:
    bubble_sort.values=to_sort
    sorted_values = bubble_sort.execute()
    assert expected == sorted_values
