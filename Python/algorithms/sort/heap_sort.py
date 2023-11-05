from typing import List


class HeapSort:
    @staticmethod
    def sort(values: List[int]) -> List[int]:
        n = len(values)
        sorted_values = list(values)
        i = n // 2 - 1
        while i >= 0:
            sorted_values = HeapSort.heapify(sorted_values, n, i)
            i -= 1

        j = n - 1
        while j > 0:
            temp = sorted_values[0]
            sorted_values[0] = sorted_values[j]
            sorted_values[j] = temp

            sorted_values = HeapSort.heapify(sorted_values, j, 0)
            j -= 1

        return sorted_values

    @staticmethod
    def heapify(values: List[int], n: int, i: int) -> List[int]:
        heap_values = list(values)
        largest_index = i
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < n and heap_values[left_index] > heap_values[largest_index]:
            largest_index = left_index

        if right_index < n and heap_values[right_index] > heap_values[largest_index]:
            largest_index = right_index

        if largest_index != i:
            swap = heap_values[i]
            heap_values[i] = heap_values[largest_index]
            heap_values[largest_index] = swap

            return HeapSort.heapify(heap_values, n, largest_index)
        return heap_values
