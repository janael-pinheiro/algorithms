from typing import List


class SelectionSort:

    @staticmethod
    def sort(values: List[int]) -> List[int]:
        n = len(values)
        for i in range(0, n-1):
            min_index = i
            for j in range(i+1, n):
                if values[j] < values[min_index]:
                    min_index = j

            temp = values[min_index]
            values[min_index] = values[i]
            values[i] = temp
        return values
