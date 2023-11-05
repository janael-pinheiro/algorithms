from typing import List


class MergeSort:

    @staticmethod
    def sort(values: List[int], left: int, right: int) -> List[int]:
        if left == right:
            return [values[left]]
        
        middle = (left + right) // 2
        left_array = MergeSort.sort(values, left, middle)
        right_array = MergeSort.sort(values, middle + 1, right)

        return MergeSort.merge_two_arrays(left_array, right_array)

    @staticmethod
    def merge_two_arrays(left_array: List[int], right_array: List[int]) -> List[int]:
        sorted_array: List[int] = []
        i, j = 0, 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                sorted_array.append(left_array[i])
                i += 1
            else:
                sorted_array.append(right_array[j])
                j += 1

        if i == len(left_array):
            while j < len(right_array):
                sorted_array.append(right_array[j])
                j += 1

        if j == len(right_array):
            while i < len(left_array):
                sorted_array.append(left_array[i])
                i += 1

        return sorted_array
