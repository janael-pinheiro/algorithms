from typing import List


class QuickSort:
    def __init__(self) -> None:
        self.values: List[int] = [None]
        self.pivot: int = 0

    def execute(self) -> any:
        pass

    def sort(self, values: List[int], left: int, right: int) -> List[int]:
        self.values = values
        self.i = left
        self.j = right
        self.pivot = self.values[left]

        while self.i <= self.j:
            while self.values[self.i] < self.pivot:
                self.i += 1
            while self.values[self.j] > self.pivot:
                self.j -= 1

            if self.i <= self.j:
                self.values[self.i], self.values[self.j] = self.values[self.j], self.values[self.i]
                self.i += 1
                self.j -= 1

        if left < self.j:
            self.sort(self.values, left, self.j)

        if self.i < right:
            self.sort(self.values, self.i, right)

        return self.values
