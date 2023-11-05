from algorithms.algorithms import AlgorithmsInterface
from typing import List


class InsertionSort(AlgorithmsInterface):
    def __init__(self):
        self.__values: List[int] = [None]

    def execute(self) -> any:
        return self.__sort()

    def __sort(self) -> List[int]:
        n = len(self.values)
        for i in range(1, n):
            j = i - 1
            value = self.values[i]
            while j >= 0 and self.values[j] > value:
                self.values[j + 1] = self.values[j]
                j = j - 1
            self.values[j + 1] = value
        return self.values

    @property
    def values(self) -> List[int]:
        return self.__values

    @values.setter
    def values(self, values: List[int]):
        self.__values = values
