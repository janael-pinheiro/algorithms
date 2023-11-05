from typing import List


class RecursiveSelectionSort:

    @staticmethod
    def sort(values: List[int], current_index=0) -> List[int]:
        sorted_values = list(values)
        if current_index == len(sorted_values)-1:
            return sorted_values
        min_index = RecursiveSelectionSort.recursive_selection(sorted_values, current_index, current_index + 1)
        sorted_values[min_index], sorted_values[current_index] = (
            sorted_values[current_index],
            sorted_values[min_index])
        return RecursiveSelectionSort.sort(sorted_values, current_index+1)

    @staticmethod
    def recursive_selection(values: List[int], min_index: int, current_index: int) -> int:
        if current_index == len(values) - 1:
            if values[current_index] < values[min_index]:
                return current_index
            return min_index

        next_index = current_index + 1
        if values[current_index] < values[min_index]:
            return RecursiveSelectionSort.recursive_selection(values, current_index, next_index)
        else:
            return RecursiveSelectionSort.recursive_selection(values, min_index, next_index)
