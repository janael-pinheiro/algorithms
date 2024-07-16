import pytest

from tests.sort.resources.sort_data import test_data


@pytest.mark.parametrize("to_sort,expected", test_data)
def test_given_tim_sort_array_return_sorted_array(tim_sort, to_sort, expected) -> None:
    tim_sort.values = to_sort
    tim_sort.min_run_length = 2
    sorted_values = tim_sort.execute()
    assert sorted_values == expected


def test_given_tim_sort_and_no_array_raise_exception(tim_sort) -> None:
    tim_sort.values = None
    with pytest.raises(ValueError):
        tim_sort.execute()
