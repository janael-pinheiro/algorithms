import string
from random import choice

from algorithms.search.simulated_annealing import SimulatedAnnealing, compute_energy, Neighbor

import pytest


@pytest.fixture(scope="function")
def simulated_annealing(request):
    return SimulatedAnnealing(
        current_solution="".join([choice(string.ascii_lowercase) for _ in range(len(request.param))]),
        target=request.param,
        maximum_temperature=100,
        minimum_temperature=0,
        minimum_energy=0,
        energy_function=compute_energy,
        get_neighbor_function=Neighbor().get_neighbor)
