from algorithms.algorithms import AlgorithmsInterface
from typing import List


class BubbleSort(AlgorithmsInterface):
    def __init__(self) -> None:
        self.__has_changed: bool = False
        self.__values: List[int] = [None]
        self.__array_length: int = 0

    def execute(self) -> any:
        return self.__sort()

    def __sort(self) -> List[int]:
        self.__array_length = len(self.__values) - 1
        FIRST_INDEX: int = 0
        while self.__array_length > FIRST_INDEX:
            for index in range(FIRST_INDEX, self.__array_length):
                if self.__should_swap_positions(
                        self.__values[index],
                        self.__values[index+1]):
                    self.__swap_positions(
                        current_index=index,
                        next_index=index+1)
                    self.__has_changed = True
            if not self.__has_changed:
                break
            self.__has_changed = False
            self.__array_length -= 1
        return self.__values

    def __should_swap_positions(self, current_value: int, next_value: int) -> bool:
        return current_value > next_value

    def __swap_positions(self, current_index: int, next_index: int):
        self.__values[current_index], self.__values[next_index] =\
            self.__values[next_index], self.__values[current_index]

    @property
    def values(self) -> None:
        return self.__values

    @values.setter
    def values(self, values: List[int]) -> None:
        self.__values = values
