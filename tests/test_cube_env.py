import pytest
from sim.turns import U, U_prime, U2
from sim.cube_env import create_cube
import numpy as np

#testing commmand: cd .. followed by python -m pytest tests/test_cube_env.py
def test_order_4_identity():
    starting_cube = create_cube()
    moved_cube = U(U(U(U(create_cube()))))
    assert np.array_equal(moved_cube, starting_cube)

    moved_cube = U_prime(U_prime(U_prime(U_prime(create_cube()))))
    assert np.array_equal(moved_cube, starting_cube)

def test_inverse_identity():
    base_cube = create_cube()
    assert np.array_equal(U(U_prime(create_cube())), base_cube)
    assert np.array_equal(U_prime(U(create_cube())), base_cube)

def test_double_turn():
    starting_cube = create_cube()
    U_double = U(U(starting_cube))
    U_prime_double = U_prime(U_prime(starting_cube))
    U_two = U2(starting_cube)
    positions = [U_double, U_prime_double, U_two]
    assert all(np.array_equal(positions[0], a) for a in positions[1: ])