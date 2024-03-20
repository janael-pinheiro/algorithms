import pytest


@pytest.mark.parametrize("simulated_annealing", ["pneumonoultramicroscopicsilicovolcanoconiosis"], indirect=True)
def test_simulated_annealing(simulated_annealing):
    target = simulated_annealing.target
    found_solution = simulated_annealing.execute()
    assert target == found_solution
