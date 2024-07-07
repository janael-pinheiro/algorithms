from dataclasses import dataclass, field
from typing import List

from algorithms.algorithms import AlgorithmsInterface
from algorithms.sort.insertion_sort import InsertionSort


@dataclass
class BucketSort(AlgorithmsInterface):
    is_float: bool = True
    values: List[int] = None
    number_buckets: int = None
    insertion_sort: InsertionSort = field(default_factory=InsertionSort)

    def execute(self) -> any:
        return self.__sort(self.values)

    def __sort(self, values: List[int]) -> List[int]:
        sorted_values = []
        if self.is_float:
            buckets = [[] for _ in range(10)]
            for value in values:
                index = int(value * 10)
                buckets[index-1].append(value)
            for index, bucket in enumerate(buckets):
                if len(bucket) > 0:
                    self.insertion_sort.values = bucket
                    buckets[index] = self.insertion_sort.execute()
                    sorted_values.extend(buckets[index])
        else:
            minimum = min(values)
            maximum = max(values)
            range_v = ((maximum - minimum) // self.number_buckets) + 1
            buckets = [[] for _ in range(self.number_buckets)]
            for value in values:
                index: int = self.__get_index(minimum, value, range_v)
                buckets[index].append(value)
            for index, bucket in enumerate(buckets):
                self.insertion_sort.values = bucket
                buckets[index] = self.insertion_sort.execute()
                sorted_values.extend(buckets[index])
        return sorted_values

    def __get_index(self, minimum: int, value: int, range_value: int) -> int:
        index = (value - minimum) // range_value
        return min(index, self.number_buckets-1)
