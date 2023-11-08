from typing import List, Tuple
from functools import reduce


class FunctionalSelectionSort:

    @staticmethod
    def sort(values: List[Tuple[int, int]]) -> List[int]:
        sorted_values = list(values)
        if len(sorted_values) == 1:
            return [sorted_values[0][1]]
        min_index, min_value = FunctionalSelectionSort.recursive_selection(sorted_values)
        remaining_values: List[Tuple[int, int]] = list(filter(lambda x: x[0] != min_index, sorted_values))
        return [min_value] + FunctionalSelectionSort.sort(remaining_values)

    @staticmethod
    def recursive_selection(values: List[Tuple[int, int]]) -> Tuple[int, int]:
        filtered_values = list(filter(lambda x: x[1] < values[0][1], values))
        if len(filtered_values) == 1:
            return filtered_values[0]
        elif len(filtered_values) == 0:
            return values[0]
        return FunctionalSelectionSort.recursive_selection(filtered_values)
