from abc import ABC, abstractmethod


class AlgorithmsInterface(ABC):
    """Algorithms interface"""
    @abstractmethod
    def execute(self) -> any:
        """"Execute the algorithm"""
