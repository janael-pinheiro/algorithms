import string
from dataclasses import dataclass, field
from math import exp
from random import choice, randint, random
from typing import Set, Callable, List

from Levenshtein import distance


@dataclass
class SimulatedAnnealing:
    target: str
    current_solution: str
    maximum_temperature: float
    minimum_temperature: float
    minimum_energy: int
    energy_function: Callable[[str, str], int]
    get_neighbor_function: Callable[[str], str]
    alpha: float = field(default=0.01)

    def __post_init__(self):
        self.__current_energy = self.energy_function(self.target, self.current_solution)
        self.__best_solution = self.current_solution
        self.__best_energy = self.__current_energy
        self.__current_temperature = self.maximum_temperature

    def execute(self) -> str:
        steps = 1
        while self.__should_continue():
            neighbor = self.get_neighbor_function(self.current_solution)
            neighbor_energy = self.energy_function(self.target, neighbor)
            delta_energy = neighbor_energy - self.__current_energy
            if delta_energy < 0:
                self.__update(neighbor, neighbor_energy)
            else:
                if exp(-delta_energy/self.__current_temperature) > random():
                    self.__update(neighbor, neighbor_energy)
            self.__current_temperature /= 1 + self.alpha
            steps += 1
        print(f"Steps: {steps}.")
        return self.__best_solution

    def __update(self, neighbor: str, neighbor_energy: int):
        self.current_solution = neighbor
        self.__current_energy = neighbor_energy
        if neighbor_energy < self.__best_energy:
            self.__update_best(neighbor, neighbor_energy)

    def __update_best(self, neighbor: str, neighbor_energy: int):
        self.__best_solution = neighbor
        self.__best_energy = neighbor_energy

    def __should_continue(self) -> bool:
        return self.__current_temperature > self.minimum_temperature and\
            self.__current_energy > self.minimum_energy


@dataclass
class Neighbor:
    __lower_case_letters: str = field(default=string.ascii_lowercase)
    __cache: Set[str] = field(default_factory=set)

    def get_neighbor(self, current_solution: str) -> str:
        index: int = randint(0, len(current_solution)-1)
        split_solution = [letter for letter in current_solution]
        split_solution[index] = choice(self.__lower_case_letters)
        neighbor = "".join(split_solution)
        if neighbor in self.__cache:
            self.get_neighbor(neighbor)
        self.__cache.add(neighbor)
        return neighbor


def compute_energy(target_solution: str, neighbor: str) -> int:
    return distance(target_solution.lower(), neighbor.lower())


if __name__ == "__main__":
    target = "pneumonoultramicroscopicsilicovolcanoconiosi"
    simulated_annealing = SimulatedAnnealing(
        current_solution="".join([choice(string.ascii_lowercase) for _ in range(len(target))]),
        target=target,
        maximum_temperature=100,
        minimum_temperature=0,
        minimum_energy=0,
        energy_function=compute_energy,
        get_neighbor_function=Neighbor().get_neighbor)
    solution = simulated_annealing.execute()
    assert target == solution
