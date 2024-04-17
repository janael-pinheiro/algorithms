import pytest

from tests.sort.resources.sort_data import test_data, test_float_data


@pytest.mark.parametrize("to_sort,expected", test_data)
def test_given_bucket_sort_array_return_sorted_array(bucket_sort, to_sort, expected) -> None:
    bucket_sort.values = to_sort
    bucket_sort.is_float = False
    bucket_sort.number_buckets = 5
    sorted_values = bucket_sort.execute()
    assert expected == sorted_values


@pytest.mark.parametrize("to_sort,expected", test_float_data)
def test_given_bucket_sort_float_array_return_sorted_array(bucket_sort, to_sort, expected) -> None:
    bucket_sort.values = to_sort
    bucket_sort.is_float = True
    bucket_sort.number_buckets = 5
    sorted_values = bucket_sort.execute()
    assert expected == sorted_values