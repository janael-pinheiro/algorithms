from dataclasses import dataclass, field
from typing import List

from algorithms.algorithms import  AlgorithmsInterface
from algorithms.sort.insertion_sort import InsertionSort


@dataclass
class TimSort(AlgorithmsInterface):
    values: List[int] = None
    min_run_length: int = None
    insertion_sort: InsertionSort = field(default_factory=InsertionSort)

    def execute(self) -> any:
        if self.values is None:
            raise ValueError("You need to provide the values to be sorted.")
        self.values = list(self.values)
        run_length = self.__compute_number_runs()
        self.__sort_runs(run_length)
        self.__merge_runs(run_length)
        return self.values

    def __sort_runs(self, run_length: int):
        for start in range(0, len(self.values), run_length):
            end = min(len(self.values) - 1, start + run_length - 1)
            self.insertion_sort.values = self.values[start: end + 1]
            self.insertion_sort.execute()
            self.values[start: end + 1] = self.insertion_sort.values

    def __compute_number_runs(self):
        run_length = len(self.values)
        remainder = 0
        while run_length > self.min_run_length:
            if run_length % 2 != 0:
                remainder = 1
            run_length = run_length // 2
        return run_length + remainder

    def __merge_runs(self, merge_size: int):
        array_length = len(self.values)
        while merge_size < array_length:
            for left in range(0, array_length, merge_size * 2):
                middle = left + merge_size - 1
                right = min(array_length, left + (2 * merge_size) - 1)
                if middle < right:
                    self.__merge(left, middle, right)
            merge_size *= 2

    def __merge(self, left: int, middle: int, right: int):
        left_array = self.values[left: middle+1]
        right_array = self.values[middle+1: right+1]
        left_index = 0
        right_index = 0
        merged_values = []
        while left_index < len(left_array) and right_index < len(right_array):
            left_value = left_array[left_index]
            right_value = right_array[right_index]
            if left_value < right_value:
                merged_values.append(left_value)
                left_index += 1
            else:
                merged_values.append(right_value)
                right_index += 1
        for i in range(left_index, len(left_array)):
            merged_values.append(left_array[i])

        for j in range(right_index, len(right_array)):
            merged_values.append(right_array[j])
        self.values[left: right+1] = merged_values
