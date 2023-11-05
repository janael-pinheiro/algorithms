from typing import List


class CountingSort:
    @staticmethod
    def sort(values: List[int]) -> List[int]:
        length = len(values)
        maximum = max(values)
        count_array = [0 for _ in range(maximum+1)]

        for i in range(length):
            count_array[values[i]] += 1

        for j in range(1, maximum+1):
            count_array[j] += count_array[j-1]

        output_array = [0 for _ in range(length)]

        k = length - 1
        while k >= 0:
            output_array[count_array[values[k]] - 1] = values[k]
            count_array[values[k]] -= 1
            k -= 1

        return output_array
